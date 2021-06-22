from typing import Any
from webob import Request, Response


def generic_no_access_view(request: Request, response: Response, **kwargs) -> dict:
    response.status_code = 403
    response.content_type = 'application/json'
    return {
        'status': 403,
        'message': 'No Access',
    }

def generic_method_not_allowed_view(request: Request, response: Response, **kwargs) -> dict:
    response.status_code = 405
    response.content_type = 'application/json'
    return {
        'status': 405,
        'message': 'Method Not Allowed',
    }
