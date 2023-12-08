import requests
import time
from bs4 import BeautifulSoup
from random import sample 
import pandas as pd 
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import json
import csv
from datetime import datetime
import re
from selenium_stealth import stealth


path = "../webscraping_outputs-Z"
os.chdir(path)
finalfile = "ZillowSelenium" + "_" + "{:%Y_%h_%d_%H-%M-%S}".format(datetime.now()) +".csv"

#Create a list that will hold the results

results = []
titleSelector = "h1.Text-c11n-8-84-3__sc-aiai24-0"
descSelector = "div.building-description"
linkSelector = "div.StyledPropertyCardDataWrapper-c11n-8-84-3__sc-1omp4c3-0"
url ="https://www.zillow.com/philadelphia-pa/rentals/"

url2 = "https://www.zillow.com/philadelphia-pa/for_sale/"

# Inspect the zillow website and figure out the number pages for rental ads use
# In the Charlotte example, there are a total of 20 pages so I set the range at 21
### --Providence Adu

for page in range(1,21,1):
    
    print("This is page: " + str(page))
    
    #Identify the Zillow URL of your City, it should follow this format:
    # 1. Default Zillow url : https://www.zillow.com/
    # 2. Name of your City: eg. charlotte-nc, atlanta-ga
    # 3. Pass the page number 
    # 4. Add the "_p" that is a default thing with the Zillow website 
    # 5. In a sample URL on page 15 for example will be like: https://www.zillow.com/charlotte-nc/rentals/15_p/

    page = str(page) + '_p/'
    
    # Here we are going to utilize the selenium. To automate the interaction behavior of a web browser you would
    # need a web driver. Each browser has a webdriver, in my case I am using google chrome so I download the web driver
    # from this website "https://chromedriver.storage.googleapis.com/index.html?path=98.0.4758.80/" 
    
    # After downloading and extracting the web drive(chromdriver.exe) you use the webdrive.Chrome() method to initiate
    # the chrome browser and pass the path where the driver is saved.
    
    driver = webdriver.Chrome()
    textDriver = webdriver.Chrome()
    # CraiglistBrowser.maximize_window()

    # After the browser has been launched use the get() to pass the url 
    print(f"Urls:\n")
    page_links = []
    for url in [url,url2]: # getListingType():
        print(f"\t\t{url+page}\n")
        browser = driver.get(url+page)
        html = driver.execute_script("return document.documentElement.outerHTML")
        soup = BeautifulSoup(html, 'html.parser')

        for item in soup.select(linkSelector):
            l = item.select("a")[0].attrs["href"]
            if not(l.startswith("https://")):
                l = "https://www.zillow.com"+l
            page_links.append(l)

    for link in page_links:
        ovPage = textDriver.get(link)
        textSoup = BeautifulSoup(textDriver.page_source,"html.parser")

        if len(textSoup.select("div.px-captcha-container")) > 0:
            time.sleep(0.3)
            continue
        else:
        
            title = textSoup.select(titleSelector)[0].text
            text = textSoup.select(descSelector)[0].text

            results.append({
                "title": title,
                "description": text,
                "url": link
            })
            print(f"title: {title}\nlink{link}")

        time.sleep(0.3)
        print(textDriver.getWebHandle())

    textDriver.close()

    time.sleep(0.5)

Zillowdata =  pd.DataFrame(results)
Zillowdata.to_csv(finalfile, index = False)
