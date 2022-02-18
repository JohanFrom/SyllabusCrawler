# Needed modules
from flask import Flask
from app.config import Config

# Function for creating the app
def create_app():
    app = Flask(__name__)
    app.config.from_object(Config) # Gets the config data
    
    # Import the different blueprints
    from app.home.home import index
    from app.syllabuscrawler.Routes import scraper
    
    # Register the blueprint
    app.register_blueprint(index)
    app.register_blueprint(scraper)
    
    return app