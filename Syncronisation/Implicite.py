import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.maximize_window()
driver.implicitly_wait(20)
driver.get('https:www.google.ca')
time.sleep(4)
#driver.find_element(By.XPATH,'//input[@name="q"]').send_keys("selenium")
#time.sleep(4)
driver.find_element(By.NAME,'q').send_keys("selenium")
searchegoogle=driver.find_element(By.NAME,'q')
searchegoogle.send_keys('selenium')
searchegoogle.submit()
time.sleep(4)
resultlink=driver.find_element(By.XPATH,'//h3[text()="selenium"]')
resultlink.click()
time.sleep(4)
driver.close()