from typing import List


class Solution:

    def missingNumber(self, arr: List[int]) -> int:
        total = (arr[0] + arr[-1]) * (len(arr) + 1) // 2
        return total - sum(arr)
