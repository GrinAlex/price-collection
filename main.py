# main.py
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



# Import parsing settings
from parsing_settings import get_parsing_settings

# Parsing scripts
from parsers.varus_parser import parse_varus
from parsers.silpo_parser import parse_silpo
# parsers.ashan_parser import parse_ashan

# Import writer to csv file
from save_to_file import write_data_to_file 


driver = webdriver.Firefox()

# Loop by parsing settings
for parsing_setting_line in get_parsing_settings():
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

driver.close()



"""

# Initialize variables
net = "Varus"
urls = ["https://varus.ua/tistechtka", "https://varus.ua/torti"]
curr_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
pause_time = 20  # seconds

# Empty data list to store product cards
data = []

# Initialize parsing count
parsintg_count = 0

driver = webdriver.Firefox()

for url in urls:
    data.extend(parse_varus(driver, url, pause_time))

driver.close()

# Specify the CSV file name
filename = "data.csv"

# Extract fieldnames from the first dictionary
fieldnames = data[0].keys()

# Write to CSV
with open(filename, mode="w", newline="", encoding="utf-8") as file:
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()  # write header row
    writer.writerows(data)  # write data rows

"""