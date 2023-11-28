import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.proxy import Proxy, ProxyType

import os
from datetime import datetime

options = Options()
options.add_experimental_option("detach", True)
options.add_argument("--headless")
options.add_argument("--disable-gpu")
# options.add_argument("--disable-extensions")
# options.add_argument("--disable-infobars")
# options.add_argument("--disable-notifications")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

def verify_title():
    driver.get("https://account.garena.com/recovery#/")
    # driver.get("https://efast.vietinbank.vn/user-unlock")
    driver.implicitly_wait(5)
    # driver.maximize_window()
    directory = "imagesData"
    # Kiểm tra nếu thư mục không tồn tại thì tạo mới
    if not os.path.exists(directory):
        os.makedirs(directory)

    for i in range(20):
        btn_link = driver.find_element("xpath", '//*[@id="main"]/div[1]/form/div[2]/div[1]/div')
        # btn_link = driver.find_element("xpath", '//*[@id="reload_href"]')
        btn_link.click()
        time.sleep(1.5)

        img_link = driver.find_element("xpath", '//*[@id="main"]/div[1]/form/div[2]/div[1]/img')
        # img_link = driver.find_element("xpath", '//*[@id="id-home"]/main/section/div[2]/div/div/div/form/div[1]/div[5]/div/div[1]/img')
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        file_name = f"anh_{timestamp}_{i + 1}.png"
        file_path = os.path.join(directory, file_name)
        img_link.screenshot(file_path)
        driver.refresh()

if __name__ == '__main__':
    verify_title()
    time.sleep(5)
    driver.quit()
