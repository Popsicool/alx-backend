from flask import Flask, render_template, request, g
from flask_babel import Babel
from pytz import timezone as tz, exceptions, utc
from datetime import datetime
import locale

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}

class Config:
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"

app = Flask(__name__)
app.config.from_object(Config)


def get_locale():
    locale =  request.args.get('locale')
    if locale in app.config['LANGUAGES']:
        return locale
    if g.user is not None:
        return g.user['locale']
    locale = request.headers.get('locale', None)
    if locale in app.config["LANGUAGES"]:
        return locale

    return request.accept_languages.best_match(app.config['LANGUAGES'])


def get_timezone():
    timezone =  request.args.get('timezone')
    if timezone:
        try:
            return tz(timezone).zone
        except exceptions.UnknownTimeZoneError:
            pass
    if g.user is not None:
        try:
            return tz(g.user['timezone']).zone
        except exceptions.UnknownTimeZoneError:
            pass
    return app.config['BABEL_DEFAULT_TIMEZONE']

def get_user():
    user_id = request.args.get("login_as", None)
    try:
        user_id = int(user_id)
    except:
        return None
    if user_id and int(user_id) and int(user_id) in users.keys():
        return (users.get(int(user_id)))
    return None

@app.before_request
def before_request():
    user = get_user()
    if user:
        g.user = user
    else:
        g.user = None
    time_now = utc.localize(datetime.utcnow())
    time = time_now.astimezone(tz(get_timezone()))
    locale.setlocale(locale.LC_TIME, (get_locale(), 'UTF-8'))
    fmt = "%b %d, %Y %I:%M:%S %p"
    g.time = time.strftime(fmt)

babel = Babel(app,  locale_selector=get_locale, timezone_selector=get_timezone)

@app.route('/', strict_slashes=False)
def index():
    return render_template('index.html')

if __name__ == "__main__":
    app.run()
