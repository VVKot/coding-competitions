def binary_search(arr, num, left, right):
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == num:
            return mid
        if arr[mid] > num:
            right = mid - 1
        else:
            left = mid + 1
    return -1

def get_shift_point(shift_arr):
    left = 0
    right = len(shift_arr) - 1
    while left < right:
        mid = (left + right) // 2
        if shift_arr[mid] > shift_arr[left]:
            left = mid
        else:
            right = mid
    return left

def shifted_arr_search(shift_arr, num):
    if not shift_arr:
        return -1
    shift_point = get_shift_point(shift_arr)
    left = right = 0
    if num >= shift_arr[0] and num <= shift_arr[shift_point]:
        left = 0
        right = shift_point
    else:
        left = shift_point + 1
        right = len(shift_arr) - 1
    return binary_search(shift_arr, num, left, right)
