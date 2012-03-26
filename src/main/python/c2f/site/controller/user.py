## -*- coding: utf-8 -*-

import logging
from c2f.site import app, template, request
from c2f.site.model.user import User as UserModel

logger = logging.getLogger(__name__)

@app.route("/user/register")
def register(data = {}):
    return template("user/register.tpl", data)


@app.route("/user/register", method="POST")
def register_process():
    data = {}
    
    data['email'] = request.forms.email.strip()
    data['name'] = request.forms.name.strip()
    data['password'] = request.forms.password.strip()
    
    user_model = UserModel()
    id = user_model.save(data['name'], data['email'])
    
    error = {}
    error['0'] = "Nome invalido !"
    error['1'] = "Inserido Id: %s" % id
    
    
    data['error'] = error
    
    #on error
    return register(data)