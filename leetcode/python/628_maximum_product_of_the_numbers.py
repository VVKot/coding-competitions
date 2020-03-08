from typing import List


class Solution:

    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort()
        positive_product = nums[-1] * nums[-2] * nums[-3]
        maybe_negative_product = nums[-1] * nums[0] * nums[1]
        return max(positive_product, maybe_negative_product)
