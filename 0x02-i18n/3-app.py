#!/usr/bin/env python3
""" 2. get local from request """
from flask import Flask, render_template, request
from flask_babel import Babel, _


class Config:
    """ Config class for app """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__)
app.config.from_object(Config)
app.url_map.strict_slashes = False
babel = Babel(app)


@babel.localeselector
def get_locale() -> str:
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def home() -> str:
    return render_template('3-index.html', locale=get_locale())


if __name__ == '__main__':
    app.run(debug=True)
