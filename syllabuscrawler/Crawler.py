from termcolor import colored
import requests
from bs4 import BeautifulSoup
from googlesearch import search


#Klasser: HTML-scrape och .pdf-scrape

class Crawler:    
    
    def print_search_word(keyword):
        print("Keyword:", colored(keyword, "green"))
        
    def get_hrefs(keyword):
        #query = "Geeksforgeeks"
 
        for j in search(keyword, tld="co.in", num=10, stop=10, pause=2):
            print(j)
        
    
    
        
    