# Needed modules
from app import create_app
from termcolor import colored

app = create_app() # Creates app

# Startar servern automatiskt och kör den i debug-mode
# Starts the server automatically and run it in debug mode
if __name__ == "__main__":
    print(colored("== Running in debug mode ==", "yellow"))
    app.run(debug=True)