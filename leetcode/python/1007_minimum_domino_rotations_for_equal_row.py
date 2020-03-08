"""
T: O(N)
S: O(1)

First, we have to find all candidates for being a number
which is the same for all rows. Note that it can be at a maximum two of them.
After that, we check the number of mismatches for each of the candidates
for each row. The minimum of all of that is the result.
"""


from typing import List


class Solution:

    ROTATION_NOT_POSSIBLE = -1

    def minDominoRotations(self, A: List[int], B: List[int]) -> int:
        N = len(A)
        possible_equal = set([A[0], B[0]])
        for i in range(1, N):
            possible_equal &= set([A[i], B[i]])
        if not possible_equal:
            return self.ROTATION_NOT_POSSIBLE
        min_rotations = N
        for num in possible_equal:
            for row in (A, B):
                curr_mismatch = 0
                for domino in row:
                    curr_mismatch += domino != num
                min_rotations = min(min_rotations, curr_mismatch)
        return min_rotations
