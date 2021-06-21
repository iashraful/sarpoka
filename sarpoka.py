from webob import Request, Response
from utils.parsers import parse_query_string


class Sarpoka:
    """
    *******************
    ***** SARPOKA *****
    *******************

    This is Python micro framework for making customized web apps.
    """

    def __init__(self):
        self.routes = {}

    def route(self, path):
        def wrapper(handler):
            self.routes[path] = handler
            return handler

        return wrapper

    def __call__(self, environ: dict, start_response):
        request = Request(environ)

        response = self.handle_request(request)

        return response(environ, start_response)

    def handle_request(self, request: Request) -> Response:
        requested_path = request.environ.get('PATH_INFO', '/')
        query_params = request.environ.get('QUERY_STRING', '')
        kwargs = {
            'query': {}
        }

        response = Response()
        view_func = self.routes.get(requested_path)
        if not view_func:
            response.text = '404 not found.'
            return response
        kwargs['query'] = parse_query_string(query_string=query_params)
        print(kwargs)
        response.text = view_func(request, response, **kwargs)
        return response
