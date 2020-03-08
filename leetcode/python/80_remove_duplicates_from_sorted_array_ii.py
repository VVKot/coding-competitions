"""
T: O(N)
S: O(1)

We can overwrite the array using constant space by remembering the last insert
position. After that, the only thing that we should check is the number of the
same elements that we have seen so far.
"""

from typing import List


class Solution:

    def removeDuplicates(self, nums: List[int]) -> int:
        insert_idx = 0
        prev_num = 0
        prev_count = 0
        for num in nums:
            if num != prev_num:
                prev_num = num
                prev_count = 0
            prev_count += 1
            if prev_count <= 2:
                nums[insert_idx] = num
                insert_idx += 1
        return insert_idx
