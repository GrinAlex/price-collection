from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

# silpo_parser.py
def parse_silpo(driver, category_url, city_name, shop_address, pause_time):

    driver.get(category_url)
   # WebDriverWait(driver, 30).until(lambda d: d.find_element(By.ID, "category-menu-button"))
    time.sleep(60)  
    
    data = []
    
    #Прибрати кукі
    while True:
        try:
            driver.find_element(By.XPATH, '/html/body/sf-shop-silpo-root/shop-silpo-root-shell/silpo-shell-main/div/div[3]/silpo-shell-cookies-banner/div/button[1]').click()
        except:
            break    
    time.sleep(5)  
    
    
    
    #Прокрутка сторінки
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
    
    
    
    #Дістати інфу
    elems = driver.find_element(By.CSS_SELECTOR, "div.products-list")
    product_cards = elems.find_elements(By.CLASS_NAME, "products-list__item")
        
    for product in product_cards:
        if not product.is_displayed():
            continue
            
        product_info = {
            'name': product.find_element(By.CLASS_NAME, "product-card__title").text,
            # 'quantity': product.find_element(By.CLASS_NAME, "sf-product-card__quantity").text,
            'regular_price': product.find_element(By.CLASS_NAME, "product-card-price__displayPrice").text.split(" ")[0] if product.find_elements(By.CLASS_NAME, "product-card-price__displayPrice") else '',
            'old_price': product.find_element(By.CLASS_NAME, "product-card-price__displayOldPrice").text if product.find_elements(By.CLASS_NAME, "product-card-price__displayOldPrice") else '',
            'special_price': product.find_element(By.CLASS_NAME, "product-card-price__displayPrice").text.split(" ")[0] if product.find_elements(By.CLASS_NAME, "product-card-price__displayPrice") else '',
            'special_text': product.find_element(By.CLASS_NAME, "ft-typo-14-semibold").text if product.find_elements(By.CLASS_NAME, "ft-typo-14-semibold") else ''
            }
        
        data.append(product_info)
                
    print(data)
    

    return data