from typing import List


class Solution:

    def removeDuplicates(self, nums: List[int]) -> int:
        prev = float('inf')
        write = same_count = 0
        for num in nums:
            if num == prev:
                same_count += 1
            else:
                prev = num
                same_count = 1
            nums[write] = num
            write += 1 if same_count < 3 else 0
        return write
