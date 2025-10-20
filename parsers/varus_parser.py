from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

# varus_parser.py
def parse_varus(driver, category_url, city_name, shop_address, pause_time):
    """
    Parses the Varus website for product information.
    
    :param driver: Selenium WebDriver instance
    :param url: URL of the Varus page to parse
    :param pause_time: Time to wait after scrolling
    :return: List of dictionaries containing product information
    """
    driver.get(category_url)
    WebDriverWait(driver, 30).until(lambda d: d.find_element(By.CLASS_NAME, "sf-product-card__title"))
    
    data = []
    
    while True:
        try:
            driver.find_element(By.CSS_SELECTOR, "div.bottom-plp-block").find_element(By.TAG_NAME, "button").click()
            time.sleep(pause_time)
        except Exception as e:
            print(f"Scrolling error: {e}")
            break
    
    elems = driver.find_element(By.CLASS_NAME, "products")
    product_cards = elems.find_elements(By.CLASS_NAME, "sf-product-card")
    
    for product in product_cards:
        if not product.is_displayed():
            continue
        
        product_info = {
            'name': product.find_element(By.CLASS_NAME, "sf-product-card__title").text,
            'quantity': product.find_element(By.CLASS_NAME, "sf-product-card__quantity").text,
            'regular_price': product.find_element(By.CLASS_NAME, "sf-price__regular").text.split(" ")[0] if product.find_elements(By.CLASS_NAME, "sf-price__regular") else '',
            'old_price': product.find_element(By.CLASS_NAME, "sf-price__old").text if product.find_elements(By.CLASS_NAME, "sf-price__old") else '',
            'special_price': product.find_element(By.CLASS_NAME, "sf-price__special").text.split(" ")[0] if product.find_elements(By.CLASS_NAME, "sf-price__special") else '',
            'special_text': product.find_element(By.CLASS_NAME, "sf-product-card__badge_text").text if product.find_elements(By.CLASS_NAME, "sf-product-card__badge_text") else ''
        }
        
        data.append(product_info)
    
    return data