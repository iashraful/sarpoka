from typing import List


def parse_query_string(query_string: str) -> dict:
    _query_dict = { 
        _each.split('=')[0]: _each.split('=')[1] for _each in query_string.split('&') if _each and len(_each.split('=')) > 1
    }
    return _query_dict


def get_lower_from_list(upper_array_items: List[str]) -> List[str]:
    return list(map(lambda x: x.lower(), upper_array_items))