from flask import Flask

app = Flask(__name__)

@app.route('/welcome')
def say_welcome():
    """Return simple "welcome" Greeting."""
    
    return "welcome"

@app.route('/welcome/home')
def say_welcome_home():
    """Return "welcome home" Greeting."""

    return "welcome home"

@app.route('/welcome/back')
def say_welcome_back():
    """Return "welcome back" Greeting."""

    return "welcome back"