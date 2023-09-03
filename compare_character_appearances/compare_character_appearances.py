import requests
from bs4 import BeautifulSoup
import csv
from datetime import datetime
import re
from config import CHARATERS

def get_dates_from_url(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")

    # Assuming the dates are in <li> tags, you might need to adjust this based on the actual structure
    dates = []
    # date_elements = soup.find_all("li")
    date_elements = soup.find_all(
        "a", title=lambda value: value and value.startswith("Episode")
    )
    for a in date_elements:
        year = a.find_previous("h2")
        dates.append(f"{a.get_text().strip()} {year.get_text().strip()}")

    return dates


def parse_date(date_str):
    # Check for two part episodes
    match = re.search(r"\((\d)\)", date_str)
    episode_part = match.group(1) if match else None

    # Clean the date string
    cleaned_date_str = (
        date_str.replace("th", "")
        .replace("st", "")
        .replace("nd", "")
        .replace("rd", "")
        .replace(f"({episode_part})", "")
        .strip()
    )

    # Parse the cleaned date string
    date_obj = datetime.strptime(cleaned_date_str, "%Y %a %d %b")

    return str(date_obj.date())


def write_dates_to_csv(common_dates):
    # remove [] from end of date and sort by year
    dates = []
    for date in sorted(common_dates):
        date = date[:-2]
        date = date[-4:] + " " + date[:-4]
        dates.append(date)

    sorted_dates = sorted(dates, key=parse_date)

    # write to csv
    file_name = ""

    for character in CHARATERS:
        file_name += list(character.keys())[0] + "_"
    file_name += "common_dates.csv"

    print("Writing common dates to file: " + file_name)

    with open(file_name, "a", newline="", encoding="utf-8") as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerows([[date] for date in sorted_dates])


def main():
    date_sets = []

    for character in CHARATERS:
        date_sets.append(get_dates_from_url(list(character.values())[0]))

    # Finding common dates
    common_dates = set.intersection(*map(set, date_sets))

    write_dates_to_csv(common_dates)


if __name__ == "__main__":
    main()
