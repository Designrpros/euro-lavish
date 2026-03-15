import os
import re
import urllib.request
from bs4 import BeautifulSoup
from datetime import datetime
import time

BASE_DIR = '/home/vegar/.openclaw/workspace/costofliving/europa/docs'

# Target metrics we want to extract from Numbeo
METRICS = {
    "Rent": "Apartment (1 bedroom) in City Centre",
    "Meal": "Meal, Inexpensive Restaurant",
    "Beer": "Domestic Beer (0.5 liter draught)",
    "Coffee": "Cappuccino (regular)",
    "Transport": "One-way Ticket (Local Transport)",
    "Cinema": "Cinema, International Release, 1 Seat"
}

def fetch_numbeo_data(city_name, country_name=None):
    """Fetches and parses Numbeo data for a given city."""
    # Format city for URL (e.g., "Novi Sad" -> "Novi-Sad")
    city_url = city_name.replace(" ", "-")
    url = f"https://www.numbeo.com/cost-of-living/in/{city_url}"
    
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/91.0'}
    
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=10) as response:
            html = response.read().decode('utf-8')
    except Exception as e:
        print(f"  [X] Could not fetch {url}: {e}")
        return None

    soup = BeautifulSoup(html, 'html.parser')
    data_table = soup.find('table', class_='data_wide_table')
    
    if not data_table:
        print(f"  [X] Could not find data table on {url}")
        return None

    results = {}
    rows = data_table.find_all('tr')
    for row in rows:
        tds = row.find_all('td')
        if len(tds) >= 2:
            item_name = tds[0].text.strip()
            item_price = tds[1].text.strip()
            
            # Map Numbeo rows to our simplified metrics
            for metric_key, numbeo_label in METRICS.items():
                if numbeo_label in item_name:
                    # Clean the price string (e.g., "5.00 €" -> "5€" or "1,200 €" -> "1200€")
                    clean_price = item_price.replace('\xa0', ' ').split(' ')[0].replace(',', '')
                    # Note: we might need to handle local currencies if requested, 
                    # but baseline we preserve the number and add the symbol later.
                    # Numbeo usually defaults to EUR if accessed from EUR IP, or we can force currency in URL ?displayCurrency=EUR
                    results[metric_key] = clean_price
                    
    return results if len(results) > 0 else None

def update_markdown_file(filepath, city_name, new_data):
    """Replaces old prices with new prices in the markdown table safely."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    original_content = content
    
    # Update the table rows
    for metric, new_price in new_data.items():
        if not new_price or new_price == '?': continue
        
        # Regex to find: | Metric | [old_price]€ | ...
        # Handling the optional RSD column in some Serbian cities
        # Pattern looks for: | Metric | <anything up to €> |
        row_pattern = rf'(\|\s*{metric}(?:(?!\n).)*?\|\s*)([\d\.]+)(€?\s*\|)'
        
        def repl(match):
            prefix = match.group(1)
            suffix = match.group(3)
            # Add € if it's missing in the suffix but should be there
            if '€' not in suffix and '€' not in new_price:
                new_val = f"{new_price}€"
            else:
                new_val = new_price
            return f"{prefix}{new_val}{suffix}"

        content = re.sub(row_pattern, repl, content, flags=re.IGNORECASE)

    # Update the timestamp
    current_month_year = datetime.now().strftime("%B %Y")
    timestamp_pattern = r'\*Data: Numbeo\.com, .*\*'
    new_timestamp = f"*Data: Numbeo.com, {current_month_year}*"
    content = re.sub(timestamp_pattern, new_timestamp, content)

    if content != original_content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        return True
    return False

def run_sync():
    print("Starting Automated Data Sync Engine...")
    updated_files = 0
    total_files = 0
    
    for root, dirs, files in os.walk(BASE_DIR):
        if 'cities' in root or 'cities' in dirs:
            target_dir = os.path.join(root, 'cities') if 'cities' in dirs else root
            for f in os.listdir(target_dir):
                if f.endswith('.md'):
                    total_files += 1
                    filepath = os.path.join(target_dir, f)
                    
                    # Extract city name from filename
                    city_base = f.replace('.md', '')
                    # Capitalize properly (e.g., novi-sad -> Novi Sad)
                    city_name = " ".join([word.capitalize() for word in city_base.split('-')])
                    
                    print(f"Scraping data for {city_name}...")
                    
                    data = fetch_numbeo_data(city_name)
                    if data:
                        if update_markdown_file(filepath, city_name, data):
                            updated_files += 1
                            print(f"  [+] Updated {city_name} successfully!")
                        else:
                            print(f"  [-] No changes needed for {city_name}")
                    
                    # Be polite to the server
                    time.sleep(1)
                    
    print(f"\nSync Complete! Updated {updated_files} out of {total_files} cities.")

if __name__ == "__main__":
    run_sync()
