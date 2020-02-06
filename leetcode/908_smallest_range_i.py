"""
T: O(N)
S: O(1)

To find out the difference between extremes in the end,
we first find that difference in the starting array. We
also can find out by how much we csn shrink this difference -
by 2K, since we can add numbers up to K magnitude to both extemes.
After that, we have to check if the distance didn't become negative
because in that case we can make it exactly zero by applying smaller numbers.
"""

from typing import List


class Solution:

    def smallestRangeI(self, A: List[int], K: int) -> int:
        return max(max(A) - min(A) - 2 * K, 0)
