from typing import List


class Solution:

    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total & 1:
            return False
        target = total / 2
        complements = set([0])
        for num in nums:
            sums_with_num = set()
            for comp in complements:
                curr_sum = comp + num
                if curr_sum == target:
                    return True
                if curr_sum < target:
                    sums_with_num.add(curr_sum)
            complements |= sums_with_num
        return False
