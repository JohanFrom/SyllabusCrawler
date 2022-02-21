from termcolor import colored
from googlesearch import search
from syllabuscrawler.HTMLScraper import HTMLScraper
from syllabuscrawler.PDFScraper import PDFScraper

class Crawler:    

    def print_search_word(keyword, pages):
        print("Keyword:", colored(keyword, "green"))
        print("Amount of pages:", colored(pages, "green"))
        
    def scrape_google(keyword, pages):
        empty_list = []
        count = 0
        try:
            for link in search(keyword, tld="co.in", num=pages, stop=pages, pause=2):
                count += 1
                print(f"{count}. {colored(link, 'cyan')}")
                if ".pdf" in link:
                    pdf_scrape_result = PDFScraper.pdf_scraper(link)
                    empty_list.append(pdf_scrape_result)
                else:
                    html_scrape_result = HTMLScraper.html_scraper(link)
                    empty_list.append(html_scrape_result)
        except (TypeError, ValueError) as e:
            empty_list.append(e)
            print("")
            print(colored("--------------------------- [ Error Message ] --------------------------", 'red'))
            print(e)
            print(colored("--------------------------[ End Error Message ]-------------------------", 'red'))
            print("")
            
        return empty_list

            
            
        
    
    
        
    