"""
T: O(N)
S: O(N)

We use a descending stack to remember the numbers that we have seen that do not
have the next greater element so far. Once we see an element that is greater
than some of the stack, we pop those elements and add a current element to the
stack. In this way, we maintain the invariant of only descending elements
in the stack.
"""
import collections
from typing import Dict, List


class Solution:

    def nextGreaterElement(self, nums1: List[int],
                           nums2: List[int]) -> List[int]:
        next_greater = collections.defaultdict(
            lambda: -1)  # type: Dict[int, int]
        stack = []  # type: List[int]
        for num in nums2:
            while stack and stack[-1] < num:
                next_greater[stack.pop()] = num
            stack.append(num)
        return [next_greater[num] for num in nums1]
