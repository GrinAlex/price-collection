from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import datetime, time

# varus_parser.py
def parse_varus(driver, category_name, category_url, city_name, shop_address, pause_time):
    """
    Parses the Varus website for product information.
    """

    curr_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    driver.get(category_url)
    WebDriverWait(driver, 30).until(lambda d: d.find_element(By.CLASS_NAME, "sf-product-card__title"))
    
    data = []
    
    # Блок адрес
    address_button = driver.find_element(By.CSS_SELECTOR, "p.swl__address")
    address_button.click()
    time.sleep(pause_time)

    # Блок самовивозу
    address_block = driver.find_element(By.CSS_SELECTOR, "div.radio-switcher-square")
    self_delivery = address_block.find_elements(By.CSS_SELECTOR, "div.radio-switcher-square__input")[1]
    self_delivery.click()

    # Вибір міста
    city_block = driver.find_element(By.CSS_SELECTOR, "div.m-input-autocomplete__chevron")
    city_block.click()
    time.sleep(pause_time)

    # Знаходження переліку міст та клік по місту Київ
    city_list = driver.find_elements(By.CSS_SELECTOR, "li.m-input-autocomplete__autocomplete-item")
    for city in city_list:
        if city.text == city_name:
            city.click()
            break
    time.sleep(pause_time)

    # Вибір магазину
    shop_list = driver.find_element(By.CSS_SELECTOR, "div.m-locate-switcher-shop__smooth")
    shop_list.click()
    time.sleep(pause_time)

    # Знаходження магазину та клік
    shop_list =shop_list.find_elements(By.CSS_SELECTOR, "li.m-input-autocomplete__autocomplete-item")
    for shop in shop_list:
        if shop.text == shop_address:
            shop.click()
            break
    time.sleep(pause_time)

    # До покупок
    button_to_shop = driver.find_element(By.CSS_SELECTOR, "div.shp-save")
    if button_to_shop.text == "До покупок":
        button_to_shop.click()
    time.sleep(pause_time)

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
        
        name = product.find_element(By.CLASS_NAME, "sf-product-card__title").text
        quantity = product.find_element(By.CLASS_NAME, "sf-product-card__quantity").text
        regular_price = product.find_element(By.CLASS_NAME, "sf-price__regular").text.split(" ")[0] if product.find_elements(By.CLASS_NAME, "sf-price__regular") else ''
        old_price = product.find_element(By.CLASS_NAME, "sf-price__old").text if product.find_elements(By.CLASS_NAME, "sf-price__old") else ''
        special_price = product.find_element(By.CLASS_NAME, "sf-price__special").text.split(" ")[0] if product.find_elements(By.CLASS_NAME, "sf-price__special") else ''
        special_text = product.find_element(By.CLASS_NAME, "sf-product-card__badge_text").text if product.find_elements(By.CLASS_NAME, "sf-product-card__badge_text") else ''

        if regular_price == '':
            regular_price = old_price

        if special_price == '':
            is_promo = False
        else:
            is_promo = True

        product_info = {
            'net': "Varus",
            'city': city_name,
            'shop_address': shop_address,
            'category': category_name,
            'product': name,
            'quantity': quantity,
            'regular_price': regular_price,
            'special_price': special_price,
            'is_promo': is_promo,
            'special_text': special_text,
            'log_date': curr_time
        }
        
        data.append(product_info)
    
    return data


if __name__ == "__main__":
    driver = webdriver.Firefox()
    category_name = "Торти"
    category_url = "https://varus.ua/torti"
    city_name = "Дніпро"
    shop_address = "вул. Панікахи, 15"
    pause_time = 10
    
    products = parse_varus(driver, category_name, category_url, city_name, shop_address, pause_time)

    driver.quit()