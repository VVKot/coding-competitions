from typing import List


class Solution:

    def rotate(self, nums: List[int], k: int) -> None:
        k %= len(nums)
        nums[k:], nums[:k] = nums[:-k], nums[-k:]
