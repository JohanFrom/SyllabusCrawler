__author__ = "Johan From and Fredrik Bramell" 

# Modules
from termcolor import colored
from flask import Flask, render_template, request
from googlesearch import search
from pathlib import Path

# Classes
from syllabuscrawler.Crawler import Crawler
from syllabuscrawler.ExcelUtility import ExcelUtility
from syllabuscrawler.LoggerUtility import LoggerUtility

app = Flask(__name__, static_url_path='/static') # Creates app

results_list = []
keyword_list = []
url_list = []
control_list= []
search_word_list = []

@app.route("/")
def index(): 
    return render_template("index.html")

@app.route("/search", methods=["POST"])
def read_input():
    results_list.clear()
    keyword_list.clear()
    url_list.clear()
    search_word_list.clear()
    
    try:
        search_word = request.form.get("search-input")
        keyword1 = request.form.get("input-keyword1")
        keyword2 = request.form.get("input-keyword2")
        keyword3 = request.form.get("input-keyword3")
        amount_pages = int(request.form.get("amount-of-pages"))
        
        keyword_list.append(keyword1)
        keyword_list.append(keyword2)
        keyword_list.append(keyword3)
        search_word_list.append(search_word)

        Crawler.print_search_word(search_word, amount_pages, keyword_list)
        for link in search(search_word, tld="co.in", num=amount_pages, stop=amount_pages, pause=2):
            url_list.append(link)
            
        results_list.append(Crawler.scrape_google(search_word, amount_pages, keyword_list))
    
        if results_list != None:
            return render_template('index.html', result=results_list, keywords=keyword_list, search=search_word)
        else:
            return render_template('index.html')
        
                
    except Exception as e:
        LoggerUtility.print_error(e)
        return render_template('index.html', result=[['Något gick fel med att söka'], [f'Felmeddelande: {e}']])
        
@app.route("/savetoexcel", methods=["POST"])
def save_excel():
    if search_word_list == control_list:
        file_name = 'sokresultat.xlsx'
    
    file_name = f'{search_word_list[0]}.xlsx'
    path_name = str(Path.home() / 'Downloads')
    
    try:
        if results_list != control_list:
            ExcelUtility.create_excel_file(path_name, file_name)
            ExcelUtility.write_links(path_name, file_name, url_list)
            ExcelUtility.write_keywords(path_name, file_name, keyword_list)
            ExcelUtility.write_result(path_name, file_name, results_list)
            return render_template('index.html', result=[['Resultatet är sparat!'], 
                                                        [f'Filen heter: {file_name}, vilket är ditt sökord du angav'], 
                                                        [f'Ligger i katalog: {path_name}']])
        else:
            return render_template('index.html', result=[['Sparar inte ner en fil på grund av inget resultat hittat!']])
    except OSError:
        return render_template('index.html', result=[['Excel filen är öppen, var snäll och stäng filen']])
    except Exception as e:
        return render_template('index.html', result=[['Att spara resultatet misslyckades'], [f'Felmeddelande: {e}']])

if __name__ == "__main__":
    print(colored("== Running in debug mode ==", "yellow"))
    app.secret_key = "SecretKey"
    app.run(debug=True)
