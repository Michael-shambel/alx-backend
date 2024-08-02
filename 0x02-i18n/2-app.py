#!/usr/bin/env python3
"""
get_locale function with the babel.localeselector decorator.
Use request.accept_languages to determine the best match with
our supported languages.
"""
from flask import Flask, render_template, request
from flask_babel import Babel


class Config:
    """
    Config class for app
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)


babel = Babel(app)


@babel.localeselector
def get_locale():
    """Get locale from request.accept
    """
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index():
    """
    Return 2-index.html
    """
    return render_template('2-index.html', locale=get_locale())


if __name__ == '__main__':
    app.run(debug=True)
