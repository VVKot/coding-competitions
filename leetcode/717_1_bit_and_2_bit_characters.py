from typing import List


class Solution:

    def isOneBitCharacter(self, bits: List[int]) -> bool:
        i, N = 0, len(bits)
        while i < N-1:
            i += 1 + bits[i]
        return i == N-1
