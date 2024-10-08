#!/usr/bin/env python3
""" 3-app """
from flask import Flask, request
from flask_babel import Babel
from routes.route0 import app_routes


app = Flask(__name__)
babel = Babel(app)


class Config():
    """ Config class to configure babel """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)
app.register_blueprint(app_routes)


@babel.localeselector
def get_locale() -> Union[str, None]:
    """ Best match for supported languages """
    return request.accept_languages.best_match(app.config["LANGUAGES"])

if __name__ == "__main__":
    app.run(debug=True)
