# parsint_settings.py
# This script is used to load and display parsing settings from a JSON file.

import json

# Read parsing settings from a JSON file
# The JSON file should contain the structure of networks, categories, and cities for parsing
with open('parsing_setting.json', 'r', encoding='utf-8') as file:
    parsing_settings = json.load(file)


# Function to get parsing networks settings
def get_nets_parsing_settings() -> list:
    nets_settings = []
    for net in parsing_settings:
        net_info = {
            'net_name': net['net_name'],
            'net_main_url': net['url'],
            'parser': net['parser']
        }
        nets_settings.append(net_info)
    return nets_settings

# Function to get categories by network name
def get_categories_by_net_name(net_name: str) -> list:
    for net in parsing_settings:
        if net['net_name'] == net_name:
            return net['categories']
    return []


# Function to get cities by network name
def get_cities_by_net_name(net_name: str) -> list:
    for net in parsing_settings:
        if net['net_name'] == net_name:
            net_cities = []
            for city in net['cities']:
                net_cities.append(city['city_name'])
            return net_cities
    return [] 


# Function to get shops by network name and city name
def get_shops_by_net_in_city(net_name: str, city_name: str) -> list:
     for net in parsing_settings:
        if net['net_name'] == net_name:
            for city in net['cities']:
                if city['city_name'] == city_name:
                    return city['shop-address']
                return []
            return []
        return []
     return []
        


# for net in parsing_settings:
    # print(net)
    # print(f"Net: {net['net_name']}")
#     print(f"URL: {net['url']}")
#     for category in net['categories']:
#         print(f"  Category: {category['category_name']}")
#         print(f"  Category URL: {category['category_url']}")
#     print(f"Parser: {net['parser']}")
#     for city in net['cities']:
#         print(f"  City: {city['city_name']}")
#         for shop in city['shop-address']:
#             print(f"    Shop Address: {shop}")
    # print('' + '-' * 40)

# 