from PyPDF2 import PdfFileReader
import io
import requests

class PDFScraper:
    
    def pdf_scraper(url):
        request_result = requests.get( url )
        
        with io.BytesIO(request_result.content) as f:
            pdf = PdfFileReader(f)
            number_of_pages = pdf.getNumPages()
            
            for i in range(0, number_of_pages):
                pageObj = pdf.getPage(i)
                result = pageObj.extractText()    
                return result
            
            
            