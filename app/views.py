from flask import render_template
from app import app
import os

@app.route('/')
@app.route('/index')
def index():
    comics = [x[0].replace('res/','',1) for x in os.walk('res/')][1:]
    return render_template("index.html", comics=comics)
