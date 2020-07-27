#Project Page Scraper (most pages)
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium import webdriver
from bs4 import BeautifulSoup as soup
import time
import datetime
import csv

#content should be dynamic in later iterations
page_number = [1,7,12,14,21,56,57,58,61,63,64,65,66,69,71,75,77,81,82,83,84,85,89,97,98,99,100,101,102,103,104,105,107,110,111,112,145,147,148,149,158,159,171,178,179,181,218,219,220,222,224,226,227,230,239,241,281,282,283,284,285,286,287,300,303,354,354,356,371,380,381,382,383,384,385,386,387,388,421,422,423,425,428,431,432,438,485,486]

#create csv file 
filename = 'DemLab Projects Tech and Skills(all).csv' 
f = open(filename, "w")

#create headers for csv 
headers = "title, skills_needed, technologies_used, last_updated\n"
f.write(headers)

#loop through the projects
for number in page_number:
    url = 'https://www.democracylab.org/index/?section=AboutProject&id=' + str(number)
    wd = webdriver.Chrome()
    wd.get(url)


    #wait for dynamic content to load 
    try: 
        wait = WebDriverWait(wd, 20)
        element = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "AboutProjects-description")))

        #grab HTML sourecode 
        html_page = wd.page_source 
        wd.quit()

        #parse 
        page = soup(html_page, 'html.parser')

        #grab page info
        results = page.findAll("div", {"class":"AboutProjects-mainColumn"})

        #about info 
        about_container = page.findAll("p", {"class":"AboutProjects-icon-text"})
        last_updated = about_container[1].text

        #title
        title_container = results[0].findAll("div", {"class": "AboutProjects-description"})
        title = title_container[0].h1.text 

        #skills 
        skill_list = [] 
        if results[0].findAll("div", {"class": "AboutProjects-skills"}):
            skills_container = results[0].findAll("div", {"class": "AboutProjects-skills"})
            skills_list = skills_container[0].findAll("p")
            for skill in skills_list:
                skill = skill.text
                skill_list.append(skill)

        #technologies 
        tech_list = [] 
        if results[0].findAll("div", {"class":"AboutProjects-technologies"}):
            technologies_container = results[0].findAll("div", {"class":"AboutProjects-technologies"})
            technologies_list = technologies_container[0].findAll("p")
            for technology in technologies_list: 
                technology = technology.text 
                tech_list.append(technology)

        #cleaning
        if len(skill_list): 
            skill_list.remove('Skills Needed')
            all_skills = '|'.join(skill_list)
        if len(tech_list):
            tech_list.remove('Technologies Used')
            all_tech = '|'.join(tech_list)


        #write onto csv file 
        if not len(skill_list):
            f.write(title + "," + "" + "," + all_tech + "," + last_updated + "\n")
        elif not len(tech_list):
            f.write(title + "," + all_skills + "," + "" + "," + last_updated + "\n")
        elif not len(skill_list) and not len(tech_list):
            f.write(title + "," + "" + "," + "" + "," + last_updated + "\n")
        else:
            f.write(title + "," + all_skills + "," + all_tech + "," + last_updated + "\n")

       
    except TimeoutException: 
        print("took too long")
        break
f.close()


    




