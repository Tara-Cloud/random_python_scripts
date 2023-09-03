import requests
from bs4 import BeautifulSoup
import csv
from config import URLS, YEAR, SHOW


# Loop through each URL
for url in URLS:
    # Send a GET request to the URL
    response = requests.get(url)

    # Parse the HTML content with BeautifulSoup
    soup = BeautifulSoup(response.content, "html.parser")

    # Find all the div elements with a title attribute
    divs_with_title = soup.find_all("a", class_="category-page__member-link")

    # Extract content from each div
    div_contents = [div.get_text(strip=True) for div in divs_with_title]

    # Write the div contents to a CSV file
    csv_filename = f"{SHOW}_episodes_{YEAR}.csv"  
    with open(csv_filename, "a", newline="", encoding="utf-8") as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerows([[content] for content in div_contents])

    print(
        f"Scraped content from {len(div_contents)} divs and appended to {csv_filename}"
    )
