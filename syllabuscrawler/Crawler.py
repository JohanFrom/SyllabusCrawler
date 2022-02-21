from termcolor import colored
import requests
import bs4
import urllib
'''
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
'''
#Klasser: HTML-scrape och .pdf-scrape

class Crawler:    
    
    def print_search_word(keyword):
        print("Keyword:", colored(keyword, "green"))
    '''
    def Initialize_Selenium(keyword):
        s=Service("C:\Program Files (x86)\chromedriver.exe")
        op = webdriver.ChromeOptions()
        # Lägg till --headless på något sätt
        op.add_experimental_option('excludeSwitches', ['enable-logging'])
        driver = webdriver.Chrome(service=s, options=op)
        driver.maximize_window()
        driver.get("https://www.google.com/")
        driver.find_element(By.ID, "L2AGLb").click()
        select_search = driver.find_element(By.NAME, 'q')
        select_search.send_keys(keyword) # Skriv in sökord i search bar
        select_search.send_keys(Keys.RETURN)
        url = driver.current_url 
        return url
    '''
        
    def get_hrefs(url):
        request_result=requests.get( url )
        soup = bs4.BeautifulSoup(request_result.text,
                                "html.parser")
        all_hrefs = soup.find_all('a')
        print(all_hrefs)
        for i in all_hrefs:
            print(i)
        
    
    
        
    