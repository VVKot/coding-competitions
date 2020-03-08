from typing import List


class Solution:

    def findDuplicate(self, nums: List[int]) -> int:
        slow = nums[0]
        fast = nums[nums[0]]
        while slow != fast:
            slow = nums[slow]
            fast = nums[nums[fast]]
        start = 0
        while start != slow:
            slow = nums[slow]
            start = nums[start]
        return slow
