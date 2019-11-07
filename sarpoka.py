#!/usr/bin/env python
from wsgiref.simple_server import make_server

def route(**kwargs):
    def decorator(func, path='/', **kwargs):
        return run(web_app=func, path=path)
    return decorator

def render(data):
    return data.encode()

def run(web_app, path='/'):
    def app_wrapper(env, response):
        status = '200 OK'
        headers = [('Content-Type', 'text/html; charset=utf-8'),]
        response(status, headers)
        return [web_app()]
    with make_server('', 8001, app_wrapper) as httpd:
        print('Servin on http://127.0.0.1:8001')
        httpd.serve_forever()
