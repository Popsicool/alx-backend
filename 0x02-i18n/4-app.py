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
babel = Babel(app)


@babel.localeselector
def get_locale():
    '''
    get the locale language
    '''
    locale = request.args.get('locale')
    if locale in app.config['LANGUAGES']:
        return locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/', strict_slashes=False)
def index() -> str:
    '''
    index
    '''
    return render_template('4-index.html')


if __name__ == "__main__":
    '''
    run if its not imported
    '''
    app.run(port="5000", host="0.0.0.0", debug=True)
