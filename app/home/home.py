from flask import render_template, Blueprint

index = Blueprint("index", __name__)

@index.route("/")
def home_page(): 
    return render_template("index.html")