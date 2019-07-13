def flip(arr, k):
    arr[:k] = reversed(arr[:k])


def pancake_sort(arr):
    num_elements = len(arr)
    for i in range(num_elements-1):
        max_elem = max(arr[:num_elements-i])
        flip_index = arr.index(max_elem)
        flip(arr, flip_index+1)
        flip(arr, num_elements-i)
    return arr
