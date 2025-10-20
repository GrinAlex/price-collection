# parsint_settings.py
# This script is used to load and return parsing settings from a Excel file.

import pandas as pd

def get_parsing_settings(file_path = "parsing_settings.xlsx"):
    """"
    Generates parsing settings from an Excel file.
    Each setting is represented as a dictionary.
    """
    df = pd.read_excel(file_path, engine="openpyxl")
    df = df[df['ToParse'] == 1]
    for index, row in df.iterrows():
        setting_by_row = {
            "net_name": row['net_name'],
            "url": row['url'],
            "category_name": row['category_name'],
            "category_url": row['category_url'],
            "parser": row['parser'],
            "city_name": row['city_name'],
            "shop_address": row['shop_address']
        }
        yield setting_by_row



if __name__ == "__main__":
    for setting in get_parsing_settings():
        print(setting)
