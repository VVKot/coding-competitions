from typing import List


class Solution:

    def missingNumber(self, arr: List[int]) -> int:
        n = len(arr)
        d = (arr[-1] - arr[0]) // n
        left, right = 0, n
        while left < right:
            mid = (left + right) // 2
            if arr[mid] == arr[0] + d * mid:
                left = mid + 1
            else:
                right = mid
        return arr[0] + d * left
