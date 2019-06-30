from typing import List


class Solution:

    def nextGreaterElement(self,
                           nums1: List[int],
                           nums2: List[int]) -> List[int]:
        greater = {num: -1 for num in nums1}
        stack = []  # type: List[int]
        for num in nums2:
            while stack and stack[-1] < num:
                smaller = stack.pop()
                if smaller in greater:
                    greater[smaller] = num
            stack.append(num)
        return [greater[num] for num in nums1]
