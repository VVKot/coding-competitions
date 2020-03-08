import collections
from typing import Counter, List


class Solution:

    def subarraySum(self, nums: List[int], k: int) -> int:
        result = total = 0
        sum_counts = collections.Counter()  # type: Counter[int]
        sum_counts[0] = 1
        for num in nums:
            total += num
            complement = total - k
            if complement in sum_counts:
                result += sum_counts[complement]
            sum_counts[total] += 1
        return result
