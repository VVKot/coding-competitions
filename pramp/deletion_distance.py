def deletion_distance(str1, str2, cache={}):
    cache_key = (str1, str2)
    if cache_key in cache:
        return cache[cache_key]
    result = 0
    if not str1 or not str2:
        result = len(str1) + len(str2)
        cache[cache_key] = result
        return result
    char1 = str1[0]
    char2 = str2[0]
    if char1 == char2:
        result = deletion_distance(str1[1:], str2[1:], cache)
    else:
        first = deletion_distance(str1[1:], str2, cache)
        second = deletion_distance(str1, str2[1:], cache)
        result = min(first, second) + 1
    cache[cache_key] = result
    return result
