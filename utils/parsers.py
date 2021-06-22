from typing import List


def parse_query_string(query_string: str) -> dict:
    """
    Query strings are basically looks like "q=my-query&search=true". So, here it's parsing the whole strings and
    breaks into dictionary
    """
    _query_dict = {
        _each.split('=')[0]: _each.split('=')[1] for _each in query_string.split('&') if
        _each and len(_each.split('=')) > 1
    }
    return _query_dict


def get_lower_from_list(upper_array_items: List[str]) -> List[str]:
    """
    Convert a list/tuple objects to lower case character and return it.
    """
    return list(map(lambda x: x.lower(), upper_array_items))


def get_upper_from_list(lower_array_items: List[str]) -> List[str]:
    """
    Convert a list/tuple objects to upper case character and return it.
    """
    return list(map(lambda x: x.upper(), lower_array_items))
