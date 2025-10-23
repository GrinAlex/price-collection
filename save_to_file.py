import csv
from pathlib import Path

HEADER = ["net", "city", "shop_address", "category", "product", "quantity", "regular_price", "special_price", "is_promo", "special_text", "log_date"]


def create_file_with_header(filename="data.csv"):
    # Create a CSV file with header
    with open(filename, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        # Define header
        writer.writerow(HEADER)


def check_file_exists(filename="data.csv"):
    return Path(filename).is_file()


def append_data_to_file(data, filename="data.csv"):
    # Append data to CSV file
    with open(filename, mode="a", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, HEADER, quoting=csv.QUOTE_ALL)
        writer.writerows(data)


def write_data_to_file(data, filename="data.csv"):
    # Write data to CSV file (overwrite)
    if not check_file_exists(filename):
        create_file_with_header(filename)
    append_data_to_file(data, filename)


if __name__ == "__main__":
    print(check_file_exists("data.csv"))