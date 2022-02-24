from bs4 import BeautifulSoup
import requests

class HTMLScraper:
    
    def html_scraper(url):
        # Scrape
        request_result = requests.get( url )
        soup = BeautifulSoup(request_result.text, 'html.parser')
        result = soup.get_text()      
        
        data_split = result.split()
            
        # Grundläggande filtering
        removers = ["\n", "\r", "\r\n", "\n\r", "\t"]
        
        data_remove = [i for i in data_split if 
                            i not in removers]
        data_fixed = ' '.join(data_remove) 
        return data_fixed

        
        
        
        