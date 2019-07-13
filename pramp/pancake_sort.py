def flip(arr, k):
    left, right = 0, k-1
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1


def pancake_sort(arr):
    num_elements = len(arr)
    for i in range(num_elements-1):
        flip_index = get_max_index_in_prefix(arr, num_elements-i)
        flip(arr, flip_index+1)
        flip(arr, num_elements-i)
    return arr


def get_max_index_in_prefix(arr, amount_to_consider):
    max_elem, max_index = float('-inf'), -1
    for i in range(amount_to_consider):
        num = arr[i]
        if num > max_elem:
            max_elem = num
            max_index = i
    return max_index
