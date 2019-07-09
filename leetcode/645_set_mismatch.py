import collections
from typing import List


class Solution:

    def findErrorNums(self, nums: List[int]) -> List[int]:
        count = collections.Counter(nums)
        duplicated = count.most_common(1)[0][0]
        missing = -1
        for i in range(1, len(nums) + 1):
            if i not in count:
                missing = i
                break
        return [duplicated, missing]
