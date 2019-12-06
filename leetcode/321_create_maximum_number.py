"""
T: O((M+N)**3)
S: O(M+N)

The idea is to find the best possible subarray from each array.
After that, we need to compare all of the combinations of subarrays
of a size k. To do that, we take up to K number from the first subarray
and the rest from the second subarray.
"""


import collections
from typing import List


class Solution:

    def maxNumber(self,
                  nums1: List[int],
                  nums2: List[int],
                  k: int) -> List[int]:
        def get_max_array(nums, l):
            to_drop = len(nums) - l
            max_array = []
            for num in nums:
                while to_drop and max_array and max_array[-1] < num:
                    max_array.pop()
                    to_drop -= 1
                max_array.append(num)
            return collections.deque(max_array[:l])

        def merge(arr1, arr2):
            total = len(arr1) + len(arr2)
            return [max(arr1, arr2).popleft() for _ in range(total)]

        return max(merge(get_max_array(nums1, i),
                         get_max_array(nums2, k-i))
                   for i in range(k+1)
                   if i <= len(nums1) and k-i <= len(nums2))
