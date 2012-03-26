'''
Created on Mar 24, 2012

@author: rfortes
'''

from c2f.site import response, request


def get_cookie(name, **options):
    return request.get_cookie(key=name, default=None, secret=None)


def set_cookie(name, value, **options):
    response.set_cookie(name, value, secret=None, **options)


def del_cookie(name, **options):
    response.delete_cookie(key=name, **options)
