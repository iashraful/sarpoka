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
        request_path = env.get('PATH_INFO')
        status = '200 OK'
        headers = [('Content-Type', 'text/html; charset=utf-8'), ]
        response(status, headers)
        if request_path == path:
            return [web_app()]
        return [b'<h2>404 not found</h2>']

    with make_server('', 8002, app_wrapper) as httpd:
        print('Serving on http://127.0.0.1:8002')
        httpd.serve_forever()
