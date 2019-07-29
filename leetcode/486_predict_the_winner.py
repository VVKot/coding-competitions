from typing import List


class Solution:

    def PredictTheWinner(self, nums: List[int]) -> bool:
        N = len(nums)
        dp = {(i, i): val for i, val in enumerate(nums)}
        for size in range(2, N+1):
            for left in range(N-size+1):
                right = left + size - 1
                with_begin = nums[left] - dp[(left+1, right)]
                with_end = nums[right] - dp[(left, right-1)]
                dp[(left, right)] = max(with_begin, with_end)
        return dp[(0, N-1)] >= 0
