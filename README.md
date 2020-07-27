# Webscraper Tool 
Tool to scrape project information from Democracy Lab. 

## Technologies Used 
Python
Selenium 

## Status 
MVP

## Directions 
Has not been tested on Windows. 

On a Mac: 

[Install python](https://www.python.org/downloads/) 
[Install selenium](https://selenium-python.readthedocs.io/)
[Install beautiful soup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)

Clone the project on your local machine by forking and cloning this respository. Copy the SSH link, open your terminal, and type:  

```$ git clone <SSH link>```

After cloning the repository, cd into the folder.  

```$ cd selenium-tutorial```

Run the program. 

Scrape all projects: 

```$ python all_projects.py```

Scrape one project: 

```$ python project.py```

The program will scrape all id numbers associated and export title, skills needed, technologies used, and last updated time frame to a csv file. 

## Errors
Sometimes, the program will fail due to timeouts. If this happens, delete the incomplete csv file and execute the script again. 


## License 
This project is licensed under the [GNU GPL](https://www.gnu.org/licenses/gpl-3.0.en.html)

    Copyright (C) <2020>  <Kailana Kahawaii>

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.
