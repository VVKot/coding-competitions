from sys import maxsize
from typing import List


class Solution:

    def merge(self,
              nums1: List[int],
              m: int,
              nums2: List[int], n: int) -> None:
        write_pointer = m + n - 1
        nums1_pointer = m - 1
        nums2_pointer = n - 1
        while nums1_pointer >= 0 or nums2_pointer >= 0:
            first = nums1[nums1_pointer] \
                if nums1_pointer >= 0 \
                else maxsize
            second = nums2[nums2_pointer] \
                if nums2_pointer >= 0 \
                else maxsize
            if first > second:
                nums1[write_pointer] = first
                nums1_pointer -= 1
            else:
                nums1[write_pointer] = second
                nums2_pointer -= 1
            write_pointer -= 1
