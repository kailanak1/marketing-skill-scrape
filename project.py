#Project Page Scraper
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium import webdriver
from bs4 import BeautifulSoup as soup
import time

url = 'https://www.democracylab.org/index/?section=AboutProject&id=1'

wd = webdriver.Chrome()
wd.get(url)

#wait for dynamic content to load 
WebDriverWait(wd, 20).until(
    EC.visibility_of_element_located((By.CLASS_NAME, "AboutProjects-description")))

#grab HTML sourecode 
html_page = wd.page_source 
wd.quit()

#parse 
page = soup(html_page, 'html.parser')
results = page.findAll("div", {"class":"AboutProjects-mainColumn"})

#Find info 

#title
title_container = results[0].findAll("div", {"class": "AboutProjects-description"})
title = title_container[0].h1.text 
print(title)

#skills 
skills_container = results[0].findAll("div", {"class": "AboutProjects-skills"})
skills_list = skills_container[0].findAll("p")
for skill in skills_list:
    skill = skill.text
    print(skill)

#technologies 
technologies_container = results[0].findAll("div", {"class":"AboutProjects-technologies"})
technologies_list = technologies_container[0].findAll("p")
for technology in technologies_list: 
    technology = technology.text 
    print(technology)