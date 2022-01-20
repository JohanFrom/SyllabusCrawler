from re import search
import webbrowser
from bs4 import BeautifulSoup
from selenium import webdriver
import time
from selenium.webdriver.chrome.service import Service
from soupsieve import select
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


''' Globals '''
s=Service("C:\Program Files (x86)\chromedriver.exe")
op = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=s, options=op)


''' -v- BeautifulSoup -v- '''
def Scrape(url):
    titles_list = []
    soup = BeautifulSoup(url, 'html.parser')
    find_all_titles = soup.find_all("h1") # Hitta alla titlar
    
    #Lägg till titlarna i en lista
    for title in find_all_titles:
        titles_list.append(title)

    for i in titles_list:
        print(i)



''' -v- Selenium WebDriver -v- '''
def Selenium_WebDriver():
    
    Initialize_GUI()
    Search_Terms()

    while True: # While loop som håller fönstret öppet
        print(".")
        time.sleep(5)
        # Avbryt loopen med "Ctrl + C" i terminalen (temporär lösning)




def Initialize_GUI():
    chrome_options = Options()
    chrome_options.add_experimental_option("detach", True) #Håller fönstret uppe (verkar inte funka 100%)
    driver.maximize_window() 
    driver.get("https://www.google.com/") # Startar browsern - OBS använd försiktigt, inte i loopar eller liknande     


def Search_Terms():
    driver.find_element(By.ID, "L2AGLb").click() # Klickar godkänn på användaravtal/gdpr knappen
    time.sleep(5) # Paus för att undgå att eventuella bluetooth errors går in som input i keyword

    keyword = input("Sökord: ")
    if keyword:
        select_search = driver.find_element(By.NAME, 'q') # Välj google search bar
        select_search.send_keys(keyword) # Skriv in sökord i search bar
        select_search.send_keys(Keys.RETURN) # Klickar enter med sökord och gör sökning



    # 1. Scraping av resultaten
        # 1.1 Hitta och välj första söknings länken
        # 1.2 Skicka url från sidan till Scrape(url)
        # 1.3 Spara resultaten från HTML-scrape i JSON-format (ny funktion eller i Scrape() 
        ''' 
        Exempel/förslag på JSON-format 
        [
            sida1 = {
                "lärandemål": [<p> blabla </p>, <p></p>, <p></p>],
                "innehåll": [<p> blabla </p>, <p></p>, <p></p>],
                syfte: [<p> blabla </p>, <p></p>, <p></p>]
                }, 
            
            sida2 = {
                "lärandemål": [<p> blabla </p>, <p></p>, <p></p>],
                "innehåll": [<p> blabla </p>, <p></p>, <p></p>],
                "syfte": [<p> blabla </p>, <p></p>, <p></p>]
                }, 
        ]
        '''
        # 1.4 Kolla ifall PDF eller txt filer finns
        # 1.5 Gör en scrape av dessa och spara på samma sätt (om möjligt) 

    # 2. Välj nästa söknings länk
        # 2.1 Upprepa 1.1 - 1.5
        # 2.2 Gör detta n antal gånger
        
    
    

Selenium_WebDriver()