"""
T: O(NlogN)
S: O(N) - only because Python sorting works in linear time

We are exploiting constraints to create an elegant solution.
First, we create a relative order map for every number in the second list.
Any other number should come after it, so we just add the maximum value
of a number to the key for the sorting.
"""


from typing import List


class Solution:

    MAX_NUM_VALUE = 1000

    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        nums_order = {num: i for i, num in enumerate(arr2)}
        return sorted(arr1,
                      key=lambda x: nums_order.get(x, self.MAX_NUM_VALUE+x))
