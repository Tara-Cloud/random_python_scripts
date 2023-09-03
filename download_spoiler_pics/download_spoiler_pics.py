import requests
from bs4 import BeautifulSoup
import re
import os
from config import URL, KEY_WORD, DIRECTORY_NAME, REG_EX_PATTERN

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}


def download_images(img_addresses):
    # Create a directory to save the images
    if not os.path.exists(DIRECTORY_NAME):
        os.makedirs(DIRECTORY_NAME)

    for address in img_addresses:
        img_url = address
        img_name = os.path.basename(img_url)
        img_response = requests.get(img_url, headers=HEADERS, stream=True)
        with open(f"{DIRECTORY_NAME}/{img_name}", "wb") as img_file:
            for chunk in img_response.iter_content(chunk_size=8192):
                img_file.write(chunk)

    print("Download complete!")


print(f"Parsing {URL}")
soup = BeautifulSoup(requests.get(URL, headers=HEADERS).content, "html.parser")
response = requests.get(URL, headers=HEADERS)

# get soup object and convert to string
body = soup.find("body")
soup_str = str(body)

# use regex to find addresses where images are hosted
pattern = re.compile(REG_EX_PATTERN)
match = pattern.search(soup_str)

# Find all matches in the string
url_values = pattern.findall(soup_str)

print(f"Found {len(url_values)} url values")
# write hips_url_values to file
with open(f"url_values.txt", "w") as f:
    f.write(str(url_values))

download_images(url_values)
