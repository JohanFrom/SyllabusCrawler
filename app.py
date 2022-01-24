# Here runs the main code

from classes import crawler

from flask import Flask, render_template, request, flash

app = Flask(__name__, static_url_path='/static')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/', methods = ["GET", "POST"])
def read_input():
    try:
        keyword1 = request.form.get("keyword1")
        keyword2 = request.form.get("keyword2")
        keyword3 = request.form.get("keyword3")
        
        #Send seperate
        test = crawler.Scrape(keyword1, keyword2, keyword3)
        
        
        return render_template('/', result=test)
        
    except:
        flash("Something went wrong, try again!")
        return render_template('/')
        

if __name__ == '__main__':
    app.secret_key = "SecretKey"
    app.run(debug=True)