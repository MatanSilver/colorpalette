# -*- coding: utf-8 -*-
from bottle import Bottle, jinja2_view, route, request, redirect
import colorgram
import os

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
        colors = [color.rgb for color in colorgram.extract(data.file, 5)]
        colors = ['#' + hex((r<<16)+(g<<8)+b)[2:] for (r, g, b) in colors]
        s['colors'] = colors
        s.save()
    return redirect('/result')


@home_app.route('/result')
@jinja2_view('result.html')
def result():
    s = request.environ.get('beaker.session')
    colors = s.get('colors', [])
    return {'colors': colors}
