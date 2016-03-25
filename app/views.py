from flask import render_template
import random
from app import app

@app.route('/')
@app.route('/index')
def index():
    fonts = [
             "Open Sans Condensed, sans-serif;",
             "Oswald, sans-serif;",
             "Ubuntu, sans-serif;",
             "Oleo Script, sans-serif;",
            ]

    model = {
                'page_title':'Matthieu Robineau - Software Solutions',
                'font': random.choice(fonts)
            }
    return render_template('index.html',
                           model=model)
