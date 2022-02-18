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
    search_word = request.form.get("search-input")
    
    Crawler.print_search_word(search_word)
    
    return render_template("index.html")

# Starts the server automatically and run it in debug mode
if __name__ == "__main__":
    print(colored("== Running in debug mode ==", "yellow"))
    app.secret_key = "SecretKey"
    app.run(debug=True)