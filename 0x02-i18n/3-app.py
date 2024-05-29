#!/usr/bin/env python3
"""
Task 2: Get locale from request
"""

from flask import Flask, render_template, request
from flask_babel import Babel


class Config:
    """Configuration class for the Flask app."""
    DEBUG = True
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
app.url_map.strict_slashes = False
babel = Babel(app)


@babel.localeselector
def get_locale() -> str:
    """
    Determine the best match for supported languages from the request.

    Returns:
        str: The best match language code.
    """
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index() -> str:
    """
    Render the homepage.

    Returns:
        str: Rendered HTML content of the homepage.
    """
    return render_template("3-index.html")


if __name__ == "__main__":
    app.run()
