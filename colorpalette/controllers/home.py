# -*- coding: utf-8 -*-
from bottle import Bottle, jinja2_view, route, request, redirect
import colorific, os

home_app = Bottle()


@home_app.route('/')
@jinja2_view('index.html')
def index():
    return {'get_url': home_app.get_url}


@home_app.route('/upload_image', method='POST')
def upload_image():
    data = request.files.get('data')
    if data is not None:
        s = request.environ.get('beaker.session')
        colors = [colorific.rgb_to_hex(color.value) for color in colorific.extract_colors(data.file).colors]
        s['colors'] = colors
        s.save()
    return redirect('/result')


@home_app.route('/result')
@jinja2_view('result.html')
def result():
    s = request.environ.get('beaker.session')
    colors = s.get('colors', [])
    return {'colors': colors}
