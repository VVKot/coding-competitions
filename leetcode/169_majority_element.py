"""
T: O(N)
S: O(1)

Remember the last most common element, and update its count according to the
current element. When the count becomes zero, update the majority element.
In the end, the last most common item is the most common overall


T: O(N)
S: O(1)

Count the number of bits in each position and if it is a majority - set this
bit in the result. 31st bit is the sign bit, so we have to treat is separately.
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

    SIGN_BIT = 31

    def majorityElement_bit_manipulation(self, nums: List[int]) -> int:
        majority_element = 0
        minority_count = len(nums) // 2
        for bit_index in range(32):
            bit_mask = 1 << bit_index
            bits_count = sum(1 for num in nums if num & bit_mask)
            if bits_count > minority_count:
                if bit_index == self.SIGN_BIT:
                    majority_element = -(bit_mask - majority_element)
                else:
                    majority_element |= bit_mask
        return majority_element
