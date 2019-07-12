import collections
from typing import List


class Solution:

    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        dup_range = k+1
        num_count = collections.Counter(nums[:dup_range])
        if any(count > 1 for count in num_count.values()):
            return True
        nums_len = len(nums)
        for i in range(0, nums_len-dup_range):
            begin, end = nums[i], nums[i+dup_range]
            num_count[begin] -= 1
            num_count[end] += 1
            if num_count[end] > 1:
                return True
        return False
