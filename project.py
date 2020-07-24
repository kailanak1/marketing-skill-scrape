#Project Page Scraper (one page)
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium import webdriver
from bs4 import BeautifulSoup as soup
import time
import datetime

url = 'https://www.democracylab.org/index/?section=AboutProject&id=1'

wd = webdriver.Chrome()
wd.get(url)

#wait for dynamic content to load 
try: 

    WebDriverWait(wd, 20).until(
        EC.visibility_of_element_located((By.CLASS_NAME, 'SectionBody')))

    #grab HTML sourecode 
    html_page = wd.page_source 
    wd.quit()

    #parse 
    page = soup(html_page, 'html.parser')

    #check if project exists 
    wd.find_element_by_xpath("/html/body/form[1]")

    results = page.findAll("div", {"class":"AboutProjects-mainColumn"})

    #Find info 

    #about info 
    about_container = page.findAll("p", {"class":"AboutProjects-icon-text"})
    location = about_container[0].text
    last_updated = about_container[1].text


    #title
    title_container = results[0].findAll("div", {"class": "AboutProjects-description"})
    title = title_container[0].h1.text 

    #skills 
    skill_list = [] 
    skills_container = results[0].findAll("div", {"class": "AboutProjects-skills"})
    skills_list = skills_container[0].findAll("p")
    for skill in skills_list:
        skill = skill.text
        skill_list.append(skill)
    

    #technologies 
    tech_list = [] 
    technologies_container = results[0].findAll("div", {"class":"AboutProjects-technologies"})
    technologies_list = technologies_container[0].findAll("p")
    for technology in technologies_list: 
        technology = technology.text 
        tech_list.append(technology)
        

    #cleaning 
    skill_list.remove('Skills Needed')
    all_skills = '|'.join(skill_list)

    tech_list.remove('Technologies Used')
    all_tech = '|'.join(tech_list)

    all_location = location.replace(",", " ")

    #create csv file 
    filename = 'DemLab Projects Tech and Skills.csv' 
    f = open(filename, "w")

    #create headers for csv 
    headers = "title, location, skills_needed, technologies_used, last_updated\n"
    f.write(headers)


    #write onto csv file 
    f.write(title + "," + all_location + "," + all_skills + "," + all_tech + "," + last_updated + "\n")
    f.close()
except: 
    print("could not locate project")