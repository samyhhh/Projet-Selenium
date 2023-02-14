import time
from email._header_value_parser import get_attribute

import driver as driver
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.maximize_window()
driver.get('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')
time.sleep(4)
placeholder_text=(driver.find_element(By.XPATH,'//input[@name="username"]').get_attribute("placeholder"))
print(placeholder_text)
list_link=driver.find_elements(By.TAG_NAME,'a')
print(len(list_link))
for element in list_link:
    print(link.get_attibute("href"))
time.sleep(4)
driver.close()