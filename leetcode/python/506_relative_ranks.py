"""
T: O(NlogN)
S: O(N)

Remember the initial position of athlete's scores, sort scores, map places to
medal names.
"""

from typing import List


class Solution:

    def findRelativeRanks(self, nums: List[int]) -> List[str]:
        num_positions = {num: i for i, num in enumerate(nums)}
        nums.sort(reverse=True)
        relative_ranks = [""] * len(nums)
        for i, num in enumerate(nums, 1):
            position = num_positions[num]
            medal = str(i)
            if i == 1:
                medal = "Gold Medal"
            if i == 2:
                medal = "Silver Medal"
            if i == 3:
                medal = "Bronze Medal"
            relative_ranks[position] = medal
        return relative_ranks
