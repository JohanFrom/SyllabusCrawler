from flask import render_template, request, Blueprint
import syllabuscrawler.Crawler as crawler

scraper = Blueprint("scraper", __name__)

@scraper.route("/search", ["POST"])
def read_input(): 
    # Hämta form
    search_input = request.form.get("search-input") 
  
    # Skicka in i funktion
    crawler.print_search_word(search_input)

    # Filter
    return render_template("index.html")

