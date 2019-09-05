import collections
from typing import List


class Solution:

    def anagramMappings(self, A: List[int], B: List[int]) -> List[int]:
        nums = collections.defaultdict(list)
        for i, num in enumerate(B):
            nums[num].append(i)
        result = []
        for num in A:
            result.append(nums[num].pop())
        return result
