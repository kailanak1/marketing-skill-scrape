#work in progress

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium import webdriver
from bs4 import BeautifulSoup as soup
import time
import datetime
import csv


for i in range(1, 600):
    url = 'https://www.democracylab.org/index/?section=AboutProject&id=' + str(i)
    wd = webdriver.Chrome()
    wd.get(url)

    try: 
        wait = WebDriverWait(wd, 20)
        element = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "SectionBody")))

        html_page = wd.page_source 
        wd.quit()

        page = soup(html_page, 'html.parser')


        if(element[2].text == "Could not load project"): 
            print('hi')
        else: 
            print("it's a project")

        
    finally: 
        print("no project found")
        wd.quit()