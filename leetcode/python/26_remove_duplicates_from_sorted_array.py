from typing import List


class Solution:

    def removeDuplicates(self, nums: List[int]) -> int:
        prev = float('inf')
        write = -1
        for num in nums:
            if num != prev:
                prev = num
                write += 1
            nums[write] = num
        return write+1
