"""
T: O(N)
S: O(1)

Find the number of columns that are not in sorted order. This is the answer.
"""

from typing import List


class Solution:

    def minDeletionSize(self, A: List[str]) -> int:
        deletion_size = 0
        for column in zip(*A):
            for i in range(1, len(column)):
                if column[i] < column[i - 1]:
                    deletion_size += 1
                    break
        return deletion_size
