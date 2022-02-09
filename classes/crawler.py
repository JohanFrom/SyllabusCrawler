from termcolor import colored
from ast import While
from cgitb import text
from distutils.log import error
from re import search
from urllib import response
from xml.etree.ElementPath import find
from xml.sax.handler import ErrorHandler
from bs4 import BeautifulSoup
from urllib.request import Request, URLopener, urlopen
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from soupsieve import select
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException, InvalidArgumentException, NoSuchWindowException


text_list = []

''' -v- BeautifulSoup -v- '''
def Scrape(url):
    print(colored("KÖR SCRAPE med url: ", 'yellow'), url)
    
    req = Request(url, headers={'User-Agent': 'Google/98.0'})
    response = urlopen(req) # Öppna decodat som UTF-8, annars läses url som sträng
    html = response.read()
    soup = BeautifulSoup(html, 'html.parser')
    allText = soup.get_text()
    
    blacklist = ["\n", "\r", "\t"]
    formatted_output = [word for word in allText if
                        word not in blacklist]
    
    joinwords = ''.join(formatted_output)
    text_list.append(joinwords)
    

def Convert_to_JSON():
    print("Konverterar...")


def Initialize_GUI(driver):
    driver.maximize_window()
    driver.get("https://www.google.com/") # Startar browsern - OBS använd försiktigt, inte i loopar eller liknande          

def Search_Terms(keyword):
    print("")
    print("KÖR SEARCH_TERMS med keyword: ", colored(keyword, 'green'))
    if keyword != "":
        #-----------------WebDriver Setup--------------------
        try:
            for i in range(1, 5): # Antal länkar som klickas in på
                #-----------------WebDriver Setup--------------------
                s=Service("C:\Program Files (x86)\chromedriver.exe")
                op = webdriver.ChromeOptions()
                op.add_argument("--headless")
                op.add_experimental_option('excludeSwitches', ['enable-logging'])
                driver = webdriver.Chrome(service=s, options=op)
                Initialize_GUI(driver)
                #----------------------------------------------------

                driver.find_element(By.ID, "L2AGLb").click() # Klickar godkänn på googles användaravtal/gdpr knapp
                select_search = driver.find_element(By.NAME, 'q') # Välj google search bar
                
                select_search.send_keys(keyword) # Skriv in sökord i search bar
                select_search.send_keys(Keys.RETURN) # Klickar enter med sökord och gör sökning

                # Första XPATH har en extra div, därefter ser alla likadana ut
                if i <= 1:
                    xpath = f'//*[@id="rso"]/div[1]/div/div[1]/div/div[1]/div/div/div/div/div[2]/div/div/div[1]'
                elif i >= 1:
                    xpath = f'//*[@id="rso"]/div[{i}]/div/div[1]/div'          
                else:
                    pass
                    # Funkade 2022-02-09: //*[@id="rso"]/div[1]/div/div[1]/div/div[1]/div/div/div/div/div[2]/div/div/div[1]
                    # Funkade 2022-02-09: //*[@id="rso"]/div[2]/div/div[1]/div (glöm inte {i} på 2)
            
                find_results_div = driver.find_element(By.XPATH, xpath) # Hitta länken
                
                
                find_results_div.click() # Klicka in på länken
                WebDriverWait(driver, 10) # Låt sidan ladda, annars läses fel url in
                url = driver.current_url # Inklickade sidans url
                if "pdf" in url:
                    pass
                else :
                    Scrape(url) # Kalla på Scrape med nuvarande url
        except (NoSuchElementException, TypeError, InvalidArgumentException, NoSuchWindowException) as e:
            text_list.append(f"Error Message: {e}")
            print("")
            print(colored("--------------------------- [ Error Message ] --------------------------", 'red'))
            print(e)
            print(colored("--------------------------[ End Error Message ]-------------------------", 'red'))
            print("")
            


# Ända syfte är att returna resultatet av scrape
def print_scrape():
    return text_list
