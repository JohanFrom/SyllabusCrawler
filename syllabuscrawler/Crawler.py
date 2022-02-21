from termcolor import colored
from googlesearch import search
from syllabuscrawler.HTMLScraper import HTMLScraper
from syllabuscrawler.PDFScraper import PDFScraper

class Crawler:    

    def print_search_word(keyword):
        print("Keyword:", colored(keyword, "green"))
        
    def scrape_google(keyword):
        empty_list = []
        count = 0
        try:
            for link in search(keyword, tld="co.in", num=10, stop=10, pause=2):
                count += 1
                print(f"{count}. {colored(link, 'cyan')}")
                if ".pdf" in link:
                    pdf_scrape_result = PDFScraper.pdf_scraper(link)
                    empty_list.append(pdf_scrape_result)
                else:
                    html_scrape_result = HTMLScraper.html_scraper(link)
                    empty_list.append(html_scrape_result)
        except (TypeError) as e:
            print(colored("--- Error Message ---", "red"))
            print(e)
            empty_list.append(e)
            
        return empty_list

            
            
        
    
    
        
    