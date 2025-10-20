# main.py
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import csv

# Import parsing settings
from parsing_settings import get_nets_parsing_settings
from parsing_settings import get_categories_by_net_name
from parsing_settings import get_cities_by_net_name
from parsing_settings import get_shops_by_net_in_city

# Parsing scripts
from parsers.varus_parser import parse_varus
# parsers.silpo_parser import parse_silpo
# parsers.ashan_parser import parse_ashan

# Get parsing networks
nets = get_nets_parsing_settings()

# Net loop
for net in nets:
    net_name = net['net_name']
    net_main_url = net['net_main_url']
    parser = net['parser']
    print(net_name)
    
    # Get product categories by nets
    nets_categories = get_categories_by_net_name(net_name)
    # Net category loop
    for net_category in nets_categories:
        category_name = net_category['category_name']
        category_url = net_category['category_url']
        print(" ", category_name)
    
    # Get cities by net name
    net_cities = get_cities_by_net_name(net_name)
    # Net cities loop
    for city in net_cities:
        net_city = city
        print(" ", net_city)
        
        # Get shops by net in city
        net_shops = get_shops_by_net_in_city(net_name, net_city)
        # Shop loop
        for shop in net_shops:
            net_shop = shop
            print("   ", net_shop)

            # ToDo Call parser with parameters: net_name, net_main_url, parser, category_name, category_url, net_city, net_shop






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