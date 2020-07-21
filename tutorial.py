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
    skill_list = skills_container.find("ul")
    for skill in skill_list: 
        skill = skill_list.text

    print(title)
    print(skill)
    