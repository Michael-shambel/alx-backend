#!/usr/bin python3
"""
This is a simple script to test the functionality of the
the 'instantiate' the Babel object in your application.
"""
from flask import Flask, render_template
from flask_babel import Babel


class Config:
    """
    Config class for the Babel object.
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)


babel = Babel(app)

@app.route('/')
def index():
    """
    Function to render a simple HTML file.
    """
    return render_template("1-index.html")

if __name__ == "__main__":
    app.run(debug=True)
