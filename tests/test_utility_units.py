from utils.parsers import parse_query_string, get_lower_from_list


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
