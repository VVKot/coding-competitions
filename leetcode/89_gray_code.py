"""
T: O(N)
S: O(1)

Magic, needs upsolving.
"""

from typing import List


class Solution:

    def grayCode(self, n: int) -> List[int]:
        return [i ^ i >> 1 for i in range(1 << n)]
