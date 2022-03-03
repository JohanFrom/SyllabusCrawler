from termcolor import colored
from googlesearch import search
from syllabuscrawler.HTMLScraper import HTMLScraper
from syllabuscrawler.PDFScraper import PDFScraper
from syllabuscrawler.Formatter import Formatter
from syllabuscrawler.ListUtility import ListUtility
from syllabuscrawler.DataFinder import DataFinder

class Crawler:    

    def print_search_word(search_word, amount_links, keyword_list):
        print("Search word:", colored(search_word, "green"))
        print("Amount of pages:", colored(amount_links, "green"))
        print("Keywords:", colored(keyword_list, "green"))
        print("-"*50)
    
    def scrape_google(keyword, pages, keywords):
        empty_list = []
        control_list = []
        count = 0
        try:
            for link in search(keyword, tld="co.in", num=pages, stop=pages, pause=2):
                count += 1
                print(f"{count}. {colored(link, 'cyan')}")
                if ".pdf" in link:
                    pdf_scrape_result = PDFScraper.pdf_scraper(link) # Scrape
                    splitted_pdf_result = ListUtility.splitter(pdf_scrape_result) # Splitter
                    found_pdf_data = DataFinder.search_for_keyword(splitted_pdf_result, keywords)
                    if found_pdf_data != control_list:
                        empty_list.append(found_pdf_data)
                        #Formatter.format_table(link, found_pdf_data, keywords)
                    else:
                        return
                else:
                    html_scrape_result = HTMLScraper.html_scraper(link) # Scrape
                    splitted_html_result = ListUtility.splitter(html_scrape_result) # Splitter
                    found_html_data = DataFinder.search_for_keyword(splitted_html_result, keywords)
                    if found_html_data != control_list:
                        empty_list.append(found_html_data)
                        #Formatter.format_table(link, found_html_data, keywords)
                    else:
                        return
                    
        
        except Exception as e:
            print("")
            print(colored("--------------------------- [ Error Message ] --------------------------", 'red'))
            print(e)
            print(colored("--------------------------[ End Error Message ]-------------------------", 'red'))
            print("")
            
        return empty_list
        

            
            
        
    
    
        
    