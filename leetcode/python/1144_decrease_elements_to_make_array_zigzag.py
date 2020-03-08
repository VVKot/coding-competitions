from typing import List
from sys import maxsize as maxint


class Solution:

    def movesToMakeZigzag(self, nums: List[int]) -> int:
        total = 0
        N = len(nums)
        nums1 = nums[:]
        for i in range(0, N, 2):
            left = nums1[i-1] if i else maxint
            right = nums1[i+1] if i < N-1 else maxint
            me = nums1[i]
            left_diff = me - left + 1 if me >= left else 0
            right_diff = me - right + 1 if me >= right else 0
            nums1[i] -= max(left_diff, right_diff)
            total += max(left_diff, right_diff)
        total2 = 0
        nums2 = nums[:]
        for i in range(1, N, 2):
            left = nums2[i-1] if i else maxint
            right = nums2[i+1] if i < N-1 else maxint
            me = nums2[i]
            left_diff = me - left + 1 if me >= left else 0
            right_diff = me - right + 1 if me >= right else 0
            nums2[i] -= max(left_diff, right_diff)
            total2 += max(left_diff, right_diff)

        return min([total, total2])
