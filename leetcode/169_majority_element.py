"""
T: O(N)
S: O(1)

Remember the last most common element, and update its count according to the
current element. When the count becomes zero, update the majority element.
In the end, the last most common item is the most common overall
"""

from typing import List


class Solution:

    def majorityElement(self, nums: List[int]) -> int:
        majority_element = 0
        majority_count = 0
        for num in nums:
            if majority_count == 0:
                majority_element = num
            majority_count += 1 if majority_element == num else -1
        return majority_element
