from typing import List


class Solution:

    def isMajorityElement(self, nums: List[int], target: int) -> bool:
        target_count = 0
        for num in nums:
            if num == target:
                target_count += 1
            elif num > target:
                break
        return target_count > len(nums) // 2
