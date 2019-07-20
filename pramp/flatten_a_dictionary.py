def flatten_dictionary(dictionary):
    return get_flattened(dictionary, "")


def get_flattened(dic, base_path):
    result = {}
    for k, v in dic.items():
        key = get_path(base_path, k)
        if isinstance(v, dict):
            result.update(get_flattened(v, key))
        else:
            result[key] = v
    return result


def get_path(base_path, current_key):
    if base_path and current_key:
        return base_path + '.' + current_key
    return base_path or current_key
