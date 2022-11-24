from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
import csv
import selenium
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

HTMLFile = open("/Users/dhyeydixit/Desktop/allthethinggy.html", "r")

# Reading the file
index = HTMLFile.read()


driver = webdriver.Chrome(ChromeDriverManager().install())
#path = "/home/toningbasher/School/ECE491/JotScraperTHing/allthethinggy.html"

#driver.get("index")
###not working here
home = "https://www.countyoffice.org"
driver.get("https://www.countyoffice.org/il-cook-county-pharmacy/")
#driver.find_element(By.CSS_SELECTOR, "div.pagings").click()
#WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a[title='Load Next 50 of 833']"))).click()
content = index
soup = BeautifulSoup(content, "html.parser")

clinics = soup.find("div", {"class": "listings"}).find_all('a')
#clinics=soup.find("a",{"class": "title"})
#teams.extend(soup.find("table", {"id": "confs_standings_W"}).findAll('a'))
clinic_link = []
for clinic in clinics:
    clinic_link.append(home + clinic["href"])
df = pd.DataFrame(clinic_link, columns=['Clinics'])

#print(df)

number_list=[]
address_list=[]
zip_list=[]

for clinic in clinic_link:
        driver.get(clinic)
        content = driver.page_source
        soup = BeautifulSoup(content, "html.parser")
        numbers = soup.find("dd", {"class": "telephone"}).find_all('a')
        addresses = soup.find_all("span", {"class": "streetAddress"})
        zips = soup.find_all("span", {"class": "postalCode"})
       # number_list.append(numbers)
        for number in numbers:
            number_list.append(number["href"])
            #print(number_list)
        for address in addresses:  
            address_list.append(address.text)  
        for onezip in zips:
            zip_list.append(onezip.text)      
df['Phone Number'] = pd.DataFrame(number_list)
df['Address'] = pd.DataFrame(address_list)
df['Zipcode'] = pd.DataFrame(zip_list)

df.to_csv('/Users/dhyeydixit/Desktop/zipandphone.csv',index=True)