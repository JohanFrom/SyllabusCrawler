# Here runs the main code
from flask import Flask, render_template

app = Flask(__name__, static_url_path='/static')

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.secret_key = "SecretKey"
    app.run(debug=True)