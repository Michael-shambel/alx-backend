#!/usr/bin/env python3
"""
login system is outside the scope of this project. To emulate a similar
behavior, copy the following user table in 5-app.py
"""
from flask import Flask, render_template, request, g
from flask_babel import Babel, _, lazy_gettext as _l

app = Flask(__name__)


class Config:
    """
    Configure available languages in our app.
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)
babel = Babel(app)

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user():
    """

    """
    user_id = request.args.get('login_as')
    if user_id:
        user = users.get(int(user_id))
        return user
    return None


@app.before_request
def before_request():
    """
    """
    user = get_user()
    g.user = user


@babel.localeselector
def get_locale():
    """
    """
    locale = request.args.get('locale')
    if locale in app.config['LANGUAGES']:
        return locale
    if g.user:
        locale = g.user.get('locale')
        if locale in app.config['LANGUAGES']:
            return locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index():
    """
    """
    return render_template('5-index.html')


if __name__ == '__main__':
    app.run(debug=True)
