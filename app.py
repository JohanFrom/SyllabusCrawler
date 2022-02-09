# Here runs the main code

from classes import crawler, filtration

from flask import Flask, render_template, request, flash

app = Flask(__name__, static_url_path='/static')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/read', methods = ["GET", "POST"])
def read_input():
    
    results_list = []
    search_input = request.form.get("search-input")   
    '''
    keyword1 = request.form.get("keyword1")
    keyword2 = request.form.get("keyword2")
    keyword3 = request.form.get("keyword3")
    '''
    # ------------ Scrape ---------------
    crawler.Search_Terms(search_input)
    scrape_result = crawler.print_scrape()
    # -----------------------------------
    
    # ------------ Filter ---------------
    #filter_result = filtration.filter_result(scrape_result)
    results_list.append(scrape_result)
    # -----------------------------------
    
    for results in results_list:
        if results == None:
            return render_template('index.html', result=["Something went wrong"])
        else:
            return render_template('index.html', result=results)


@app.route("/clear", methods = ["GET", "POST"])
def clear_result():  
    empty_list = []
    
    #clear_data = crawler.print_scrape()
    empty_list.append("")
    return render_template('index.html', result=empty_list)

if __name__ == '__main__':
    app.secret_key = "SecretKey"
    app.run(debug=True)