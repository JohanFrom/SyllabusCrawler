from ast import While
from cgitb import text
from distutils.log import error
from re import search
from urllib import response
from xml.sax.handler import ErrorHandler
from bs4 import BeautifulSoup
from urllib.request import URLopener, urlopen
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from soupsieve import select
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

text_list = []

''' -v- BeautifulSoup -v- '''
def Scrape(url):
    print("KÖR SCRAPE med url: ", url)
    

    response = urlopen(url) # Öppna decodat som UTF-8, annars läses url som sträng
    html = response.read()
    soup = BeautifulSoup(html, 'html.parser')
    allText = soup.get_text()
    
    blacklist = ["\n", "\r"]
    formatted_output = [word for word in allText if
                        word not in blacklist]
    
    joinwords = ''.join(formatted_output)
    text_list.append(joinwords)
    return text_list
    

def Convert_to_JSON():
    print("Konverterar...")


def Initialize_GUI(driver):
    driver.maximize_window()
    driver.get("https://www.google.com/") # Startar browsern - OBS använd försiktigt, inte i loopar eller liknande      


def Search_Terms(keyword):
    print("KÖR SEARCH_TERMS med keyword: ", keyword)
    
    if keyword != "":
        for i in range(1, 2): # Antal länkar som klickas in på
            #-----------------WebDriver Setup--------------------
            s=Service("C:\Program Files (x86)\chromedriver.exe")
            op = webdriver.ChromeOptions()
            driver = webdriver.Chrome(service=s, options=op)
            Initialize_GUI(driver)
            #----------------------------------------------------

            driver.find_element(By.ID, "L2AGLb").click() # Klickar godkänn på googles användaravtal/gdpr knapp
            select_search = driver.find_element(By.NAME, 'q') # Välj google search bar
            
            select_search.send_keys(keyword) # Skriv in sökord i search bar
            select_search.send_keys(Keys.RETURN) # Klickar enter med sökord och gör sökning

            # Första XPATH har en extra div, därefter ser alla likadana ut
            if i <= 1:
                xpath = f'/html/body/div[7]/div/div[10]/div[1]/div/div[2]/div[2]/div/div/div[{i}]/div/div/div[1]/a/div'
            elif i >= 1:
                xpath = f'/html/body/div[7]/div/div[10]/div[1]/div/div[2]/div[2]/div/div/div[{i}]/div/div[1]/div/a/div'          
            else:
                pass
                
            
            find_results_div = driver.find_element(By.XPATH, xpath) # Hitta länken
            find_results_div.click() # Klicka in på länken
            
            WebDriverWait(driver, 20) # Låt sidan ladda, annars läses fel url in
            url = driver.current_url # Inklickade sidans url
            if "pdf" in url:
                pass
            else :
                Scrape(url) # Kalla på Scrape med nuvarande url

def print_scrape():
    return text_list
