#!/usr/bin/env python3
'''
0x02. i18n
'''
from flask import Flask, render_template, request
from flask_babel import Babel


class Config:
    '''
    configuration for default values
    '''
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)


def get_locale():
    '''
    get the locale language
    '''
    return request.accept_languages.best_match(app.config['LANGUAGES'])


babel = Babel(app,  locale_selector=get_locale)


@app.route('/', strict_slashes=False)
def index() -> str:
    '''
    index
    '''
    return render_template('3-index.html')


if __name__ == "__main__":
    '''
    run if its not imported
    '''
    app.run(port="5000", host="0.0.0.0", debug=True)
