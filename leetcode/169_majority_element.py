from typing import List


class Solution:

    def majorityElement(self, nums: List[int]) -> int:
        major, count = 0, 0
        for num in nums:
            if not count:
                major, count = num, 1
            elif num == major:
                count += 1
            else:
                count -= 1
        return major
