import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.maximize_window()
driver.get('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')
list_link=driver.find_elements(By.TAG_NAME,"a")
print("lenombre de lien sur la page est: ", len(list_link))
time.sleep(4)
for link in list_link:
    print(link.text)
    print(link.get_attribute("href"))

driver.close()

