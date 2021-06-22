from webob import Request, Response
from utils.parsers import parse_query_string, get_lower_from_list
from utils.generics import generic_method_not_allowed_view


class Sarpoka:
    """
    *******************
    ***** SARPOKA *****
    *******************

    This is Python micro framework for making customized web apps.
    """

    def __init__(self):
        self.routes = {}
        self.safe_methods = ('get', 'head', 'options',)

    def route(self, path, methods=['get']):
        def wrapper(handler):
            # Making a tuple of http methods and view function
            self.routes[path] = (methods, handler,)
            return handler

        return wrapper

    def __call__(self, environ: dict, start_response):
        request = Request(environ)

        response = self.handle_request(request)

        return response(environ, start_response)

    def handle_request(self, request: Request) -> Response:
        requested_path = request.environ.get('PATH_INFO', '/')
        query_params = request.environ.get('QUERY_STRING', '')
        requested_method = request.environ.get('REQUEST_METHOD', 'options')
        kwargs = {
            'query': {}
        }

        response = Response()
        allowed_methods, view_func = self.routes.get(requested_path)
        if requested_method.lower() not in get_lower_from_list(allowed_methods):
            view_func = generic_method_not_allowed_view
        if not view_func:
            response.text = '404 not found.'
            return response
        kwargs['query'] = parse_query_string(query_string=query_params)
        response_body = view_func(request, response, **kwargs)
        if response.content_type.lower() == 'application/json':
            response.json = response_body
        else:
            response.text = str(response_body)
        return response
