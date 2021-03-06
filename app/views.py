from flask import render_template
from app import app
import os
from flask import send_from_directory
from app.comicbook import comicbook
from natsort import natsorted


@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/x-icon')


@app.route('/ios_icon.png')
def ios_icon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'ios_icon.png', mimetype='image/png')


@app.route('/swipepage.js')
def swipepage_js():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'swipepage.js', mimetype='text/javascript')


@app.route('/')
@app.route('/index')
def index():
    comics = natsorted(os.walk('res/').next()[1])
    return render_template("index.html", comics=comics)


@app.route('/<path:comic>/<f>.<ext>')
def comic_page(comic, f, ext):
    filename = f + '.' + ext
    cb = comicbook(comic, filename)
    basepath = os.path.join(app.root_path, '..', 'res', comic)
    page = os.path.join(basepath, filename)
    return render_template("comic_index.html", comicbook=cb, page=page)


@app.route('/<path:comic>/<f>.<ext>/img')
def comic_page_img(comic, f, ext):
    page = f + '.' + ext
    basepath = os.path.join(app.root_path, '..', 'res', comic)
    return send_from_directory(basepath, page)


@app.route('/<path:comic>/thumbnail')
def comic_thumbnail(comic):
    cb = comicbook(comic)
    if cb.thumbnail_path():
        basepath = os.path.join(app.root_path, '..', 'res', comic)
        return send_from_directory(basepath, cb.thumbnail_path())
    else:
        return send_from_directory(os.path.join(app.root_path, 'static'),
                                   'blank_thumbnail.gif', mimetype='image/gif')


@app.route('/<path:comic>')
def comic(comic):
    cb = comicbook(comic)
    return render_template("comic_index.html", comicbook=cb)
