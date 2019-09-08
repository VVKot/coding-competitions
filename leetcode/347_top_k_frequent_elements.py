import collections
import itertools
from typing import List


class Solution:

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        buckets = [[] for _ in nums]
        for num, freq in collections.Counter(nums).items():
            buckets[-freq].append(num)
        return list(itertools.chain(*buckets))[:k]
