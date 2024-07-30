#!/usr/bin/env python3
"""
the _ or gettext function to parametrize your templates. Use the message IDs
home_title and home_header.
"""
from flask import Flask, render_template, request
from flask_babel import Babel, _


class Config:
    """Configure available languages in our app."""
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'

app = Flask(__name__)
app.config.from_object(Config)
app.url_map.strict_slashes = False
babel = Babel(app)


@babel.localeselector
def get_locale():
    """Determine the best match with our supported languages."""
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def home():
    """Render the home page."""
    return render_template('3-index.html', locale=get_locale())


if __name__ == '__main__':
    app.run(debug=True)
