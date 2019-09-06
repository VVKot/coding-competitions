import collections
from typing import Dict, List


class Solution:

    def anagramMappings(self, A: List[int], B: List[int]) -> List[int]:
        nums = collections.defaultdict(list)  # type: Dict[int, List[int]]
        for i, num in enumerate(B):
            nums[num].append(i)
        result = []
        for num in A:
            result.append(nums[num].pop())
        return result
