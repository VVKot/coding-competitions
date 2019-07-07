import collections
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        return list(map(lambda x: x[0], collections.Counter(nums).most_common(k)))
