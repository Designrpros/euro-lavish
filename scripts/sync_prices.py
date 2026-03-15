import os
import re
import random
import requests
from bs4 import BeautifulSoup
from datetime import datetime
import time

# Dynamically find the docs directory relative to the script location
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.dirname(SCRIPT_DIR)
BASE_DIR = os.path.join(PROJECT_ROOT, 'docs')

# Target metrics we want to extract from Numbeo
METRICS = {
    "Rent": "Apartment (1 bedroom) in City Centre",
    "Meal": "Meal, Inexpensive Restaurant",
    "Beer": "Domestic Beer (0.5 liter draught)",
    "Coffee": "Cappuccino (regular)",
    "Transport": "One-way Ticket (Local Transport)",
    "Cinema": "Cinema, International Release, 1 Seat"
}

def fetch_numbeo_data(city_name):
    """Fetches and parses Numbeo data for a given city."""
    # Format city for URL (e.g., "Novi Sad" -> "Novi-Sad") 
    # Use urllib.parse.quote for cities with special characters (e.g. Košice -> Ko%C5%A1ice)
    city_url = requests.utils.quote(city_name.replace(" ", "-"))
    url = f"https://www.numbeo.com/cost-of-living/in/{city_url}?displayCurrency=EUR"
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1'
    }
    
    try:
        response = requests.get(url, headers=headers, timeout=15)
        response.raise_for_status()
        html = response.text
    except Exception as e:
        print(f"  [X] Could not fetch {url}: {e}")
        return None

    soup = BeautifulSoup(html, 'html.parser')
    data_table = soup.find('table', class_='data_wide_table')
    
    if not data_table:
        print(f"  [X] Could not find data table on {url}. Page title: {soup.title.string if soup.title else 'Unknown'}")
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
                if numbeo_label.lower() in item_name.lower():
                    # Clean the price string (e.g., "5.00 €" -> "5€" or "1,200 €" -> "1200€")
                    clean_price = item_price.replace('\xa0', ' ').split(' ')[0].replace(',', '')
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
        if os.path.basename(root) == 'cities':
            for f in files:
                if f.endswith('.md'):
                    total_files += 1
                    filepath = os.path.join(root, f)
                    
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
                    
                    # Be polite to the server to avoid Rate Limits
                    sleep_time = random.uniform(3.0, 5.0)
                    time.sleep(sleep_time)
                    
    print(f"\nSync Complete! Updated {updated_files} out of {total_files} cities.")

if __name__ == "__main__":
    run_sync()
