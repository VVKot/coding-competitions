from typing import List


class Solution:

    def productExceptSelf(self, nums: List[int]) -> List[int]:
        N = len(nums)
        products = [1] * N
        curr = nums[0]
        for i in range(1, N):
            products[i] *= curr
            curr *= nums[i]
        curr = nums[-1]
        for i in reversed(range(0, N-1)):
            products[i] *= curr
            curr *= nums[i]
        return products
