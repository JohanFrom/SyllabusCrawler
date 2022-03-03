from PyPDF2 import PdfFileReader
import io
import requests

class PDFScraper:
    
    def pdf_scraper(url):        
        request_result = requests.get( url )
        with io.BytesIO(request_result.content) as f:
            pdf = PdfFileReader(f)
            number_of_pages = pdf.getNumPages()
            for i in range(number_of_pages):
                pageObj = pdf.getPage(i)
                result = pageObj.extractText()  
                data_split = result.split()

                removers = ["\n", "\r", "\r\n", "\n\r", "\t"]
                data_remove = [i for i in data_split if 
                                    i not in removers]
                data_fixed = ' '.join(data_remove) 
                
                return data_fixed
            
            
            