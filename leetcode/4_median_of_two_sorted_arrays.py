from typing import List


class Solution:

    def findMedianSortedArrays(self,
                               nums1: List[int],
                               nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        M, N = len(nums1), len(nums2)
        total = M+N
        left, right = 0, M
        while True:
            pivot1 = (left+right) // 2
            pivot2 = (total+1) // 2 - pivot1
            left1 = nums1[pivot1-1] if pivot1 != 0 else float('-inf')
            left2 = nums2[pivot2-1] if pivot2 != 0 else float('-inf')
            right1 = nums1[pivot1] if pivot1 != M else float('inf')
            right2 = nums2[pivot2] if pivot2 != N else float('inf')
            if left1 <= right2 and left2 <= right1:
                if total & 1:
                    return max(left1, left2)
                else:
                    return (max(left1, left2) + min(right1, right2)) / 2
            elif left1 > right2:
                right = pivot1-1
            else:
                left = pivot1+1
