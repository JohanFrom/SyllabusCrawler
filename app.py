# Here runs the main code

from classes import crawler

from flask import Flask, render_template, request, flash

app = Flask(__name__, static_url_path='/static')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/read', methods = ["GET", "POST"])
def read_input():
    search_input = request.form.get("search-input")

    '''
    keyword1 = request.form.get("keyword1")
    keyword2 = request.form.get("keyword2")
    keyword3 = request.form.get("keyword3")
    '''
    
    #Send seperate
    crawler.Search_Terms(search_input)
    results_list = []
    x = crawler.print_scrape()
    results_list.append(x)

    return render_template('index.html', result=results_list)
        

if __name__ == '__main__':
    app.secret_key = "SecretKey"
    app.run(debug=True)