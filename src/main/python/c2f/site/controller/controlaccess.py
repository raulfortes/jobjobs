## -*- coding: utf-8 -*-

import logging

from c2f.site import app, template , request

logger = logging.getLogger(__name__)

@app.route("/login")
def index():
    
    return template("login.tpl")

@app.route('/login', method='POST')
def login_process():
    name     = request.forms.get('name')
    password = request.forms.get('password')
    
    if name == password:
        return "<p>Your login was correct</p>"
    else:
        return "<p>Login failed</p>"
    
class AuthenticationException( Exception ):
        pass
    
def loginrequired( fn ):
    def wrapper( *args, **kwargs ):
        #print "args:",args
        #print "kwargs:",kwargs
        print 'teste'
        #j = args[1]
        #if not j['authenticated']:
        #raise AuthenticationException( "Not authenticated" )
        #*args, **kwargs
        fn( *args, **kwargs )
    return wrapper
