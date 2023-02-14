# Ces commandes liees a l'application
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.maximize_window()
driver.get('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')
titre_page=driver.title
print(titre_page)

URL_page=driver.current_url
print(URL_page)
code_source_page=driver.page_source
time.sleep(4)
driver.close()