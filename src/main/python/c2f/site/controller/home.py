## -*- coding: utf-8 -*-

import logging
from c2f.site import app, template
from c2f.site.controller.controlaccess import loginrequired

logger = logging.getLogger(__name__)

@app.route("/")
def index():
    #view = template.get_template("home.html")
    
    #return view.render()
    return template("home.tpl")

@app.route("/logado")
@loginrequired
def index_logado():
    #view = template.get_template("home.html")
    
    #return view.render()
    return template("home.tpl")
