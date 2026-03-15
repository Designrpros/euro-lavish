import os
import re
import urllib.parse

BASE_DIR = '/home/vegar/.openclaw/workspace/costofliving/europa/docs'

# The unapproved P_IDs that are currently causing the "marker not subscribed" error
UNAPPROVED_P_IDS = [
    'p=121',  # Booking.com
    'p=125',  # TripAdvisor
    'p=285',  # Hotels.com
    'p=170'   # Lonely Planet (in case any lingering ones survived the previous swap)
]

def process_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    original_content = content

    # Regex to find all tp.media links, safely stopping at quotes, spaces, or closing parens from the Markdown
    pattern = r'(https?://tp\.media/r\?marker=710853&p=\d+&u=([^\s)"\']+))'

    def replacement(match):
        full_tp_link = match.group(1)
        encoded_dest = match.group(2)
        
        # Check if the P_ID is in the unapproved list
        if any(unapproved in full_tp_link for unapproved in UNAPPROVED_P_IDS):
            try:
                # Decode the URL (e.g., https%3A%2F%2Fwww.booking.com -> https://www.booking.com)
                clean_url = urllib.parse.unquote(encoded_dest)
                return clean_url
            except Exception as e:
                print(f"Error decoding url {encoded_dest}: {e}")
                return full_tp_link
        
        # If it's approved (like Viator p=89), leave it alone
        return full_tp_link

    # Replace all matches in the file content
    content = re.sub(pattern, replacement, content)

    if content != original_content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        return True
    return False

def run_unwrap():
    count = 0
    total = 0
    for root, dirs, files in os.walk(BASE_DIR):
        for f in files:
            if f.endswith('.md'):
                total += 1
                if process_file(os.path.join(root, f)):
                    count += 1
                    
    print(f"Unwrapped unapproved affiliate links back to clean URLs in {count} out of {total} files.")

if __name__ == "__main__":
    run_unwrap()
