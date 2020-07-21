# Selenium Tutorial 

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium import webdriver
from bs4 import BeautifulSoup as soup
import time

url = 'https://www.democracylab.org/index/?section=FindProjects'

wd = webdriver.Chrome()
wd.get(url)

#wait for dynamic content to load 
WebDriverWait(wd, 20).until(
    EC.visibility_of_element_located((By.CLASS_NAME, "ProjectCard-title")))

# #grab HTML sourecode 
html_page = wd.page_source 
wd.quit()

#parse 
page = soup(html_page, 'html.parser')
cards = page.findAll("div", {"class":"ProjectCard-root"})

#loop through the cards
for card in cards: 
    title_container = card.find("div", {"class":"ProjectCard-title"})
    title = title_container.h2.text
    skills_container = card.find("div", {"class":"ProjectCard-skills"})
    for skill in skills_container:
        skill = skills_container.text
        new_skill = skill.replace("Skills Needed","")
    print(title)
    print(new_skill)