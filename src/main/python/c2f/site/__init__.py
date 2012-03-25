## -*- coding: utf-8 -*-
#import os
#import sys
#import logging

from bottle import Bottle
#from c2f.site.config import parameters
#from c2f.api.rest_client_lib import Rest
#from c2f.site.lib.jinja2_cache import Jinja2Cache
#from jinja2.loaders import FileSystemLoader
#from jinja2.environment import Environment
#from c2f.site.controller import get_context_variables
from bottle import jinja2_view as view, jinja2_template as template
from bottle import request as bottle_request
from bottle import response as bottle_response
from bottle import redirect as bottle_redirect

app = Bottle()
request = bottle_request
response = bottle_response
redirect = bottle_redirect

#template_dir = os.path.dirname(os.path.realpath(__file__)) + '/view'
#template = Environment(loader=FileSystemLoader(template_dir), extensions=['jinja2.ext.autoescape'])

# FIXME: carregar este do config
#template.globals['dev_mode'] = parameters.getboolean('system', 'dev_mode')
#template.globals['context'] = get_context_variables

#logger.info('Template dir: ' + template_dir)