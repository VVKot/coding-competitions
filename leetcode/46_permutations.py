import itertools
from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        return list(list(perm) for perm in itertools.permutations(nums))
