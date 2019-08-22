from typing import List


class Solution:

    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        present_nums = set(nums)
        return [i for i in range(1, len(nums)+1) if i not in present_nums]
