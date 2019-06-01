from typing import List, Dict


class Solution:
    def nextGreaterElement(self,
                           nums1: List[int],
                           nums2: List[int]) -> List[int]:
        greater, stack = {}, []  # type: Dict[int, int], List[int]
        for num in nums2:
            while stack and stack[-1] < num:
                small = stack.pop()
                greater[small] = num
            stack.append(num)
        for num in stack:
            greater[num] = -1
        return [greater[x] for x in nums1]
