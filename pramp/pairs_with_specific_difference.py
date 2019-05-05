def find_pairs_with_given_difference(arr, k):
    comp = {x-k: x for x in arr}
    return [[comp[y], y] for y in arr if y in comp]
