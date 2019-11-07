from wsgiref.simple_server import make_server
from sarpoka import render, route


@route(path='/')
def foo():
    return render('<h1>Working 2</h1>')


foo()
