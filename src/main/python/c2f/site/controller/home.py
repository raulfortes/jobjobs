## -*- coding: utf-8 -*-

import logging
from c2f.site import app, template

logger = logging.getLogger(__name__)

@app.route("/")
def index():
    view = template.get_template("home.html")
    
    return view.render()
