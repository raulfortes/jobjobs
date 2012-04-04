## -*- coding: utf-8 -*-

# Controler para retornar os arquivos estáticos do site
import os
from c2f.site import app
from c2f.site.config import parameters, base_path
from bottle import static_file, abort, response


# no-cache para ambiente de desenvolvimento
def set_no_cache():
    response.set_header('Cache-Control', 'no-cache')
    response.set_header('PRAGMA', 'no-cache')


@app.get('/google0dedfa7b2c62408d.html')
def get_google():
    response._status_code_ = 200
    return response

# js release version
@app.get('/static/<filepath:path>')
def get_file(filepath):
    if parameters.getboolean('system', 'dev_mode'):
        set_no_cache()
    return static_file(filepath, root=os.path.join(base_path, 'site', 'static'))




# js release version
@app.get('/static/js/<file_name:re:[a-z]+([\-\.\_]{1}[a-z]+)*([\.\-\_]{1}[0-9]+)+\.min\.js$>')
def get_js(file_name):
    if parameters.getboolean('system', 'dev_mode'):
        set_no_cache()

    return static_file(file_name, root=os.path.join(base_path, 'site', 'static', 'release', 'js'))


# js source version
@app.get('/static/source/js/<file_name:re:[a-z]+([\-\.\_]{1}[a-z]+)*([\.\-\_]{1}[0-9]+)*(\.min)?\.js$>')
def get_source_js(file_name):
    if parameters.getboolean('system', 'dev_mode'):
        set_no_cache()
        return static_file(file_name, root=os.path.join(base_path, 'site', 'static', 'source', 'js'))
    else:
        abort(401, 'Acesso não permitido.')


# css release version
@app.get('/static/css/<file_name:re:(.*?)\.css$>')
def get_css(file_name):
    if parameters.getboolean('system', 'dev_mode'):
        set_no_cache()

    return static_file(file_name, root=os.path.join(base_path, 'site', 'static', 'css'), mimetype='text/css')


# css source version
@app.get('/static/source/css/<file_name:re:[a-z]+([\-\.\_]{1}[a-z]+)*([\.\-\_]{1}[0-9]+)*(\.min)?\.(css|less)$>')
def get_source_css(file_name):
    if parameters.getboolean('system', 'dev_mode'):
        set_no_cache()
        return static_file(file_name, root=os.path.join(base_path, 'site', 'static', 'source', 'css'), mimetype='text/css')
    else:
        abort(401, 'Acesso não permitido.')


# img release version
@app.get('/static/img/<file_name:re:[a-z]{1}[a-z0-9]+([\-\.\_]+[a-z0-9]+)*\.(png|gif|jpg|jpeg)$>')
def get_img(file_name):
    if parameters.getboolean('system', 'dev_mode'):
        set_no_cache()

    return static_file(file_name, root=os.path.join(base_path, 'site', 'static', 'release', 'img'))


# img source version
@app.get('/static/source/img/<file_name:re:[a-z]{1}[a-z0-9]+([\-\.\_]+[a-z0-9]+)*\.(png|gif|jpg|jpeg)$>')
def get_source_img(file_name):
    if parameters.getboolean('system', 'dev_mode'):
        set_no_cache()

        return static_file(file_name, root=os.path.join(base_path, 'site', 'static', 'source', 'img'))
    else:
        abort(401, 'Acesso não permitido.')
