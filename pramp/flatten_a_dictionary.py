from typing import Dict


def iterate_dict(dic: Dict[str, str], base_path: str) -> Dict[str, str]:
    result = {}
    for k, v in dic.items():
        key = base_path + "." + k
        if not base_path or not k:
            key = base_path or k
        if isinstance(v, dict):
            result.update(iterate_dict(v, key))
        else:
            result[key] = v
    return result


def flatten_dictionary(dictionary: Dict[str, str]) -> Dict[str, str]:
    return iterate_dict(dictionary, "")
