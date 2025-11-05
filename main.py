# main.py
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



# Import parsing settings
from parsing_settings import get_parsing_settings, set_parsed_row

# Parsing scripts
from parsers.varus_parser import parse_varus
from parsers.silpo_parser import parse_silpo
# parsers.ashan_parser import parse_ashan

# Import writer to csv file
from save_to_file import write_data_to_file 


driver = webdriver.Firefox()

# Loop by parsing settings
for parsing_setting_line in get_parsing_settings():
    row_number = parsing_setting_line['row_number']
    net_name = parsing_setting_line['net_name']
    net_url = parsing_setting_line['url']
    category_name = parsing_setting_line['category_name']
    category_url = parsing_setting_line['category_url']
    parser = parsing_setting_line['parser']
    city_name = parsing_setting_line['city_name']
    shop_address = parsing_setting_line['shop_address']

    # Define parcer function based on parser name
    if parser == 'varus_parser':
        data = parse_varus(driver, category_name, category_url, city_name, shop_address, pause_time=10)
    elif parser == 'silpo_parser':
        data = parse_silpo(driver, category_name, category_url, city_name, shop_address, pause_time=10)   
    
    write_data_to_file(data)

    set_parsed_row(row_number)

driver.close()

