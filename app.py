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
    try:
        
        results_list = []
        search_word = request.form.get("search-input")
        amount_pages = int(request.form.get("amount-of-pages"))

        Crawler.print_search_word(search_word, amount_pages)
        results_list = Crawler.scrape_google(search_word, amount_pages)
        
        #return render_template('index.html')
        
        # scrape_result = function -> results_list.append(scrape_result)
        
        if results_list == None:
            return render_template('index.html', result=results_list)
        else:
            return render_template('index.html', result=results_list)
    except (ValueError, TypeError) as e:
        results_list.append(e)
        print("")
        print(colored("--------------------------- [ Error Message ] --------------------------", 'red'))
        print(e)
        print(colored("--------------------------[ End Error Message ]-------------------------", 'red'))
        print("")
    

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