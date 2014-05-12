from flask import render_template
from app import app
import os
from flask import send_from_directory

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/x-icon')

@app.route('/')
@app.route('/index')
def index():
    comics = [x[0].replace('res/','',1) for x in os.walk('res/')][1:]
    return render_template("index.html", comics=comics)
