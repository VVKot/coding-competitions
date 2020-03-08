"""
T: O(N)
S: O(1)

Move two pointers from the ends of both arrays. If we reach the beginning of
either array, we should if it is the first pointer. If so, we still have more
elements to copy using the second pointer.
"""

from typing import List


class Solution:

    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        write_pointer = m + n - 1
        nums1_pointer = m - 1
        nums2_pointer = n - 1
        while nums1_pointer >= 0 and nums2_pointer >= 0:
            first = nums1[nums1_pointer]
            second = nums2[nums2_pointer]
            if first > second:
                nums1[write_pointer] = first
                nums1_pointer -= 1
            else:
                nums1[write_pointer] = second
                nums2_pointer -= 1
            write_pointer -= 1
        while nums2_pointer >= 0:
            nums1[write_pointer] = nums2[nums2_pointer]
            write_pointer -= 1
            nums2_pointer -= 1
