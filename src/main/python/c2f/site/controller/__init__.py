# -*- coding: utf8 -*-
from bottle import request

__all__ = ['home','static']

def get_context_variables():
    variables = {}
    
#    if request.get_cookie('user_details'):
#        cookie = get_client_cookie()
#        variables['client_name'] = cookie.client_name
    
    # variables['base_url'] = 'http://localhost:8080'
    
    return variables
