from bs4 import BeautifulSoup
from selenium import webdriver
import time
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

''' -- BeautifulSoup -- '''
#url = "https://www.google.com/"
#soup = BeautifulSoup(url, 'html.parser')


''' -- Selenium WebDriver -- '''
s=Service(ChromeDriverManager().install())
PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH, service=s)
chrome_options = Options()
chrome_options.add_experimental_option("detach", True) 
driver.maximize_window()


driver.get("https://www.wikipedia.com") # Startar browsern - OBS använd försiktigt


while True: # While loop som håller fönstret öppet
    print(".")
    time.sleep(5)
    # Avbryt loopen med "Ctrl + C" i terminalen (temporär lösning)