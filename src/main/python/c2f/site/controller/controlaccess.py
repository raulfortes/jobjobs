## -*- coding: utf-8 -*-

import logging

from c2f.site import app, template, request, redirect
from c2f.site.form.login import LoginForm

logger = logging.getLogger(__name__)

@app.route('/login', method=['GET', 'POST'])
def login():
    message = None
    form = LoginForm(request.POST)
    if request.method == 'POST' and form.validate():
        email = form.email.data
        password = form.password.data
        if email == password:
            redirect('/')
        else:
            message = 'Login failed !'
    return template("login.html", form=form, message=message)    


class AuthenticationException(Exception):
        pass


def loginrequired(fn):
    def wrapper(*args, **kwargs):
        #print "args:",args
        #print "kwargs:",kwargs
        print 'teste'
        #j = args[1]
        #if not j['authenticated']:
        #raise AuthenticationException( "Not authenticated" )
        #*args, **kwargs
        fn(*args, **kwargs)
    return wrapper
