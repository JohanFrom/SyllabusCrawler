from termcolor import colored
import requests
from bs4 import BeautifulSoup


#Klasser: HTML-scrape och .pdf-scrape

class Crawler:    
    
    def print_search_word(keyword):
        print("Keyword:", colored(keyword, "green"))
        
    def get_hrefs(url):
        page = requests.get("https://www.google.dz/search?q=see")
        soup = BeautifulSoup(page.content)
        import re
        links = soup.findAll("a")
        print(links)
        for link in soup.find_all("a",href=re.compile("(?<=/url\?q=)(htt.*://.*)")):
            print(re.split(":(?=http)",link["href"].replace("/url?q=","")))
        
    
    
        
    