#!/usr/bin/env python3
'''
0x02. i18n
'''
from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def index() -> str:
    '''
    index
    '''
    return render_template('0-index.html')


if __name__ == "__main__":
    '''
    run if its not imported
    '''
    app.run(port="5000", host="0.0.0.0", debug=True)
