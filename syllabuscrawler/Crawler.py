from googlesearch import search
from syllabuscrawler.LoggerUtility import LoggerUtility
from syllabuscrawler.HTMLScraper import HTMLScraper
from syllabuscrawler.PDFScraper import PDFScraper
from syllabuscrawler.DataFinder import DataFinder
from syllabuscrawler.ListUtility import ListUtility

class Crawler:    

    def print_search_word(search_word, amount_links, keyword_list):
        search_word_string = f"Search word: {search_word}"
        amount_string = f"Amount of pages: {amount_links}"
        keywords_string = f"Keywords: {keyword_list}"
        LoggerUtility.print_debug(search_word_string)
        LoggerUtility.print_debug(amount_string)
        LoggerUtility.print_debug(keywords_string)
          
    
    def scrape_google(keyword, pages, keywords):
        empty_list = []
        control_list = []
    
        for i, link in enumerate(search(keyword, tld="co.in", num=pages, stop=pages, pause=2)):
            LoggerUtility.print_debug(f"{i+1}. {link}")
            
            if ".pdf" in link:
                pdf_scrape_result = PDFScraper.pdf_scraper(link)
                splitted_pdf_data = ListUtility.list_formating(pdf_scrape_result)
                found_pdf_data = DataFinder.search_for_keyword(splitted_pdf_data, keywords)
                if found_pdf_data != control_list:
                    empty_list += found_pdf_data
            else:
                html_scrape_result = HTMLScraper.html_scraper(link)
                splitted_html_data = ListUtility.list_formating(html_scrape_result)
                found_html_data = DataFinder.search_for_keyword(splitted_html_data, keywords)
                if found_html_data != control_list:
                    empty_list += found_html_data
                    
        return empty_list

        
    