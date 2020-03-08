from typing import List


class Solution:

    def rotate(self, nums: List[int], k: int) -> None:
        N = len(nums)
        k %= N
        self.reverse(nums, 0, N-1)
        self.reverse(nums, 0, k-1)
        self.reverse(nums, k, N-1)

    def reverse(self, nums: List, left: int, right: int) -> None:
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
