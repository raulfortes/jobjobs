# -*- coding: utf8 -*-
from bottle import request
#from c2f.site.tools.cookie import get_client_cookie

#__all__ = ['home', 'product', 'department', 'search', 'static', 'admin', 'template', 'client', 'address','mysql']
__all__ = ['home','static','curriculo']

def get_context_variables():
    variables = {}
    
#    if request.get_cookie('user_details'):
#        cookie = get_client_cookie()
#        variables['client_name'] = cookie.client_name
    
    # variables['base_url'] = 'http://localhost:8080'
    
    return variables
