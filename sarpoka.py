from webob import Request, Response


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

        response = Response()
        view_func = self.routes.get(requested_path)
        if not view_func:
            response.text = '404 not found.'
            return response
        response.text = view_func(request, response)
        return response
