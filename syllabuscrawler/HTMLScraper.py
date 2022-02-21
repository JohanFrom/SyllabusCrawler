from bs4 import BeautifulSoup
import requests

class HTMLScraper:
    
    def html_scraper(url):
        request_result = requests.get( url )
        soup = BeautifulSoup(request_result.text, 'html.parser')
        result = soup.find_all('p')
        return result
        
        