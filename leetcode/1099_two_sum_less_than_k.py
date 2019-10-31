from typing import List


class Solution:

    NUMS_RANGE = 1000

    def twoSumLessThanK(self, A: List[int], K: int) -> int:
        buckets = [False] * (self.NUMS_RANGE+1)
        for num in A:
            buckets[num] = True
        nums = [num for num, is_present in enumerate(buckets) if is_present]

        i, j = 0, len(nums) - 1
        result = -1
        while i < j:
            S = nums[i] + nums[j]
            if S < K:
                result = max(result, S)
                i += 1
            else:
                j -= 1
        return result
