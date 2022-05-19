from PyPDF2 import PdfFileReader
import io
import requests
from bs4 import BeautifulSoup


class Scraper:
    
    def html_scraper(url):
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
    
    def pdf_scraper(url):        
        request_result = requests.get( url )
        with io.BytesIO(request_result.content) as f:
            pdf = PdfFileReader(f)
            number_of_pages = pdf.getNumPages()
            for i in range(number_of_pages):
                pageObj = pdf.getPage(i)
                result = pageObj.extractText()  
                
                return result    