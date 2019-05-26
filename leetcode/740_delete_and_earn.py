from collections import Counter
from typing import List


class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        nums_counter = Counter(nums)
        prevprev, prev = (float('inf'), 0), (float('inf'), 0)
        for num, count in sorted(nums_counter.items()):
            curr = num * count
            if num - 1 == prev[0]:
                curr = max(curr + prevprev[1], prev[1])
            else:
                curr += prev[1]
            prevprev, prev = prev, (num, curr)
        return prev[1]
