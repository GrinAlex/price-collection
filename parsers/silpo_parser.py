from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import datetime, time

# silpo_parser.py


def parse_silpo(driver, category_name, category_url, city_name, shop_address, pause_time):

    curr_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    driver.get(category_url)
    # WebDriverWait(driver, 30).until(lambda d: d.find_element(By.CLASS_NAME, "cookie-accept"))
    time.sleep(pause_time)

    data = []

    # Прибрати куки
    while True:
        try:
            driver.find_element(By.CLASS_NAME, "cookie-accept").click()
        except:
            break
    time.sleep(2)
    
    # Блок адрес + самовивіз
    address_button = driver.find_element(By.CLASS_NAME, "header-delivery").click()
    time.sleep(pause_time)

    self_delivery = driver.find_element(By.CLASS_NAME, 'selfDelivery').click()
    time.sleep(pause_time)

    # Вибір міста (очистити інпут і вписати місто)
    delete_addres = driver.find_element(By.CLASS_NAME, 'search-input__clear').click()
    time.sleep(pause_time)

    city_choose = driver.find_element(By.ID, "city")
    city_choose.send_keys(city_name)

    city_list = driver.find_elements(By.CLASS_NAME, "search-suggestions__item-title")
    for city in city_list:
        if city.text == city_name:
            city.click()
            break
    time.sleep(20)

    # Вибір магазину (очиститка інпута)
    address_market = driver.find_element(By.CSS_SELECTOR, 'shop-silpo-self-delivery-autocomplete.ng-star-inserted').click()
    time.sleep(1)
    while True:
        try:
            driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/ecomui-modal-component-host/div/sf-shop-silpo-remote-select-address-modal/shop-silpo-basket-select-address-modal/shop-silpo-basket-select-address/shop-silpo-basket-select-address-desktop/div/div[2]/div[1]/shop-silpo-basket-select-address-self-delivery/div/div[1]/div/shop-silpo-self-delivery-autocomplete[2]/shop-silpo-self-delivery-autocomplete-input/div/button').click()
        except:
            break
    time.sleep(1)

    # Вибір магазину (очиститка інпута)
    shop_list = driver.find_element(By.CLASS_NAME, "search-suggestions-scroll")
    time.sleep(3)
    shop_list = shop_list.find_elements(By.CLASS_NAME, "search-suggestions__item")
    for shop in shop_list:
        if shop.text == shop_address:
            shop.click()
            break
    time.sleep(3)

    # Підтвердити адресу
    button_accept = driver.find_element(By.CLASS_NAME, 'address-search-container-content__button').click()
    time.sleep(pause_time)

    # Прокрутка сторінки
    while True:
        try:
            driver.find_element(By.XPATH, '/html/body/sf-shop-silpo-root/shop-silpo-root-shell/silpo-shell-main/div/div[3]/silpo-category/silpo-catalog/div/div[2]/div/ecomui-pagination/div/button/div').click()
            time.sleep(5)
        except Exception as e:
            break

    prev_height = -1
    max_scrolls = 100
    scroll_count = 0
    while scroll_count < max_scrolls:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(3)
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == prev_height:
            break
        prev_height = new_height
        scroll_count += 1
    
    # Збір інфи
    elems = driver.find_element(By.CSS_SELECTOR, "div.products-list")
    product_cards = elems.find_elements(By.CLASS_NAME, "products-list__item")

    for product in product_cards:
        if not product.is_displayed():
            continue


        label_imgs_container = product.find_element(By.CLASS_NAME, "product-card__labels")
        label_imgs = label_imgs_container.find_elements(By.TAG_NAME, "img")
        label_text = [img.get_attribute("alt") for img in label_imgs if img.get_attribute("alt")]
        labels_texts = ', '.join(label_text)

    
        name = product.find_element(By.CLASS_NAME, "product-card__title").text
        quantity = product.find_element(By.CLASS_NAME, "ft-typo-14-semibold").text
        regular_price = product.find_element(By.CLASS_NAME, "product-card-price__displayPrice").text.split(" ")[0] if product.find_elements(By.CLASS_NAME, "product-card-price__displayPrice") else ''
        old_price = product.find_element(By.CLASS_NAME, "product-card-price__displayOldPrice").text if product.find_elements(By.CLASS_NAME, "product-card-price__displayOldPrice") else ''
        special_price = product.find_element(By.CLASS_NAME, "product-card-price__displayPrice").text.split(" ")[0] if product.find_elements(By.CLASS_NAME, "product-card-price__displayPrice") else ''
        special_text = labels_texts


        if old_price == '':
            old_price = regular_price
            special_price = ''

        if old_price == regular_price:
            is_promo = False
        else:
            is_promo = True


        product_info = {
            'net': "Сільпо",
            'city': city_name,
            'shop_address': shop_address,
            'category': category_name,
            'product': name,
            'quantity': quantity,
            'regular_price': old_price,
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
    category_url = "https://silpo.ua/category/torty-tistechka-663"
    city_name = "Бровари"
    shop_address = "вул. Київська, 156"
    pause_time = 10

    products = parse_silpo(driver, category_name, category_url, city_name, shop_address, pause_time)

    driver.quit()
