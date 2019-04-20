import math


def binary_search(arr, num):
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] > num:
            right = mid - 1
        elif arr[mid] < num:
            left = mid + 1
        else:
            return True
    return False


def get_duplicates_bs(large, small):
    result = []
    for num in small:
        if binary_search(large, num):
            result.append(num)
    return result


def get_duplicates(arr1, arr2):
    result = []
    p1, p2 = 0, 0
    len1, len2 = len(arr1), len(arr2)
    while p1 < len1 and p2 < len2:
        curr1, curr2 = arr1[p1], arr2[p2]
        if curr1 == curr2:
            result.append(curr1)
            p1 += 1
            p2 += 1
        elif curr1 < curr2:
            p1 += 1
        else:
            p2 += 1
    return result


def find_duplicates(arr1, arr2):
    len1 = len(arr1)
    len2 = len(arr2)
    # determine if we should use binary search or regular search
    if math.log(len2, 2) * len1 > len2 + len1:
        return get_duplicates(arr1, arr2)
    else:
        return get_duplicates_bs(arr2, arr1)
