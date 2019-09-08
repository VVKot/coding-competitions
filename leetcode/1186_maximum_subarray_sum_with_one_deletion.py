from typing import List


class Solution:

    def maximumSum(self, arr: List[int]) -> int:
        if all(num < 0 for num in arr):
            return max(arr)
        max_sum = with_deletion = without_deletion = 0
        for num in arr:
            if num >= 0:
                with_deletion += num
                without_deletion += num
            else:
                with_deletion = max(with_deletion+num, without_deletion)
                without_deletion = max(without_deletion+num, 0)
            max_sum = max([max_sum, with_deletion, without_deletion])
        return max_sum
