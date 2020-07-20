from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from bs4 import BeautifulSoup as soup
import time

url = 'https://www.democracylab.org/index/?section=FindProjects'

driver = webdriver.Chrome()
driver.get(url)



#wait for dynamic content to load 
try: 
    rows = WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "row"[1]))
    )
    print(rows)
except:
    driver.quit()


driver.quit()