from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup



def Search_Terms(keyword):
    print("KÖR SEARCH_TERMS med keyword: ", keyword)
    
    result_list = []

    if keyword != "":
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
        url = driver.current_url # Inklickade sidans url
        href_list = scrape_google(url)

        for url in href_list:
            print(url)
            #text = webscrape(url)
            #result_list.append(text)
    return 




def Initialize_GUI(driver):
    driver.maximize_window()
    driver.get("https://www.google.com/") # Startar browsern - OBS använd försiktigt, inte i loopar eller liknande




def scrape_google(url):
    href_list = []
    filtered_href_list = []
    req = Request(url, headers={'User-Agent': 'Google/98.0'})
    response = urlopen(req) # Öppna decodat som UTF-8, annars läses url som sträng
    html = response.read()
    soup = BeautifulSoup(html, 'html.parser')


    for link in soup.find_all('a', href=True):
        href_list.append(link['href'])


    new_list = filter_list(href_list)
    for i in new_list:
        i = i.split('q=')
        i.pop(0)
        filtered_href_list.append(i)
        
    return filtered_href_list




def webscrape(url):
    response = urlopen(url) # Öppna decodat som UTF-8, annars läses url som sträng
    html = response.read()
    soup = BeautifulSoup(html, 'html.parser')
    scrape_result = soup.get_text()
    return scrape_result




def filter_list(list):
    list = list[17:28]
    list.pop(1)
    return list