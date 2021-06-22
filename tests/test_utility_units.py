from webob import Request, Response

from utils.generics import generic_no_access_view, generic_method_not_allowed_view
from utils.parsers import parse_query_string, get_lower_from_list, get_upper_from_list


def test_parse_query_string():
    params_as_string = 'q=test&search=true&page=10'
    parsed_data = parse_query_string(params_as_string)
    assert isinstance(parsed_data, dict)
    assert parsed_data['q'] == 'test'
    assert parsed_data['search'] == 'true'
    assert parsed_data['page'] == '10'


def test_get_lower_from_list():
    data = get_lower_from_list(['A', 'b', 'C'])
    assert isinstance(data, list)
    assert data == ['a', 'b', 'c']


def test_get_upper_from_list():
    data = get_upper_from_list(['a', 'b', 'c'])
    assert isinstance(data, list)
    assert data == ['A', 'B', 'C']


def test_generic_no_access_view():
    _request = Request(environ={})
    _response = Response()
    data = generic_no_access_view(request=_request, response=_response)
    assert isinstance(data, dict)
    assert _response.status_code == 403


def test_generic_method_not_allowed_view():
    _request = Request(environ={})
    _response = Response()
    data = generic_method_not_allowed_view(request=_request, response=_response)
    assert isinstance(data, dict)
    assert _response.status_code == 405
