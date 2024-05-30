#!/usr/bin/env python3
"""flask app"""

from typing import Dict, Union
from flask import Flask, render_template, request, g
from flask_babel import Babel


class Config:
    """Flask app."""
    DEBUG = True
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user() -> Union[Dict, None]:
    """user based on a user id from query parameters."""
    login_id = request.args.get('login_as')
    return users.get(int(login_id)) if login_id else None


@app.before_request
def before_request() -> None:
    """Sinformation before each request."""
    g.user = get_user()


@babel.localeselector
def get_locale() -> str:
    """Dbest match for supported languages."""
    locale = request.args.get('locale')
    if locale in app.config['LANGUAGES']:
        return locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index() -> str:
    """main."""
    return render_template("5-index.html")


if __name__ == "__main__":
    app.run()

