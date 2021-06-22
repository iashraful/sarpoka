from utils.parsers import parse_query_string


def test_parse_query_string():
    params_as_string = 'q=test&search=true&page=10'
    parsed_data = parse_query_string(params_as_string)
    assert isinstance(parsed_data, dict)
    assert parsed_data['q'] == 'test'
    assert parsed_data['search'] == 'true'
    assert parsed_data['page'] == '10'

