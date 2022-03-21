from bs4 import BeautifulSoup
import requests

class HTMLScraper:
    
    def html_scraper(url):
        # Scrape
        request_result = requests.get( url )
        soup = BeautifulSoup(request_result.text, 'html.parser')
        
        for a in soup.select("a"):
            a.decompose()
        for s in soup.select("script"):
            s.decompose()  
        for b in soup.select("button"):
            b.decompose()
        for n in soup.select("nav"):
            n.decompose()
        for f in soup.select("form"):
            f.decompose()    
        
        result = soup.get_text()
        
        return result
        

        
        
        
        