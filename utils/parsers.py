def parse_query_string(query_string: str) -> dict:
    _query_dict = { 
        _each.split('=')[0]: _each.split('=')[1] for _each in query_string.split('&') if _each and len(_each.split('=')) > 1
    }
    return _query_dict


