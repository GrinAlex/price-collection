# parsint_settings.py
# This script is used to load and return parsing settings from a Excel file.

import pandas as pd

def get_parsing_settings(file_path = "parsing_settings.xlsx"):
    """"
    Generates parsing settings from an Excel file.
    Each setting is represented as a dictionary.
    """
    df = pd.read_excel(file_path, engine="openpyxl")
    # df_with_index = df.reset_index()
    df_with_index = df.reset_index().rename(columns={'index': 'row_number'})

    df_with_index = df_with_index[df_with_index['ToParse'] == 1]
    for index, row in df_with_index.iterrows():
        setting_by_row = {
            "row_number": row['row_number'],
            "net_name": row['net_name'],
            "url": row['url'],
            "category_name": row['category_name'],
            "category_url": row['category_url'],
            "parser": row['parser'],
            "city_name": row['city_name'],
            "shop_address": row['shop_address']
        }
        yield setting_by_row


def set_parsed_row(row_number, file_path = "parsing_settings.xlsx"):
    df = pd.read_excel(file_path)
    df.loc[row_number, 'Parsed'] = 1
    df.to_excel(file_path, index=False)



if __name__ == "__main__":
    for setting in get_parsing_settings():
        print(setting)

    set_parsed_row(2)
