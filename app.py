# Needed modules
from termcolor import colored
from flask import Flask, render_template, request

# Classes
from syllabuscrawler.Crawler import Crawler

app = Flask(__name__, static_url_path='/static') # Creates app

@app.route("/")
def index(): 
    return render_template("index.html")

@app.route("/search", methods=["POST"])
def read_input():
    #results_list = []
    search_word = request.form.get("search-input")

    Crawler.print_search_word(search_word)
    #url = Crawler.Initialize_Selenium(search_word)
    #print(url)
    Crawler.get_hrefs(search_word)
    
    return render_template('index.html')
    
    # scrape_result = function -> results_list.append(scrape_result)
    '''
    for results in results_list:
        if results == None:
            return render_template('index.html', result=["Something went wrong"])
        else:
            return render_template('index.html', result=results)
    '''

@app.route("/clear", methods=["POST"])
def clear_result():
    cleared_list = []
    cleared_list.append("")
    return render_template("index.html", result=cleared_list)
    

# Starts the server automatically and run it in debug mode
if __name__ == "__main__":
    print(colored("== Running in debug mode ==", "yellow"))
    app.secret_key = "SecretKey"
    app.run(debug=True)