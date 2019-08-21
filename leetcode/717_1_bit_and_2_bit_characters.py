from typing import List


class Solution:

    def isOneBitCharacter(self, bits: List[int]) -> bool:
        last = False
        i, N = 0, len(bits)
        while i < N:
            if bits[i] == 1:
                i += 2
                last = False
            else:
                i += 1
                last = True
        return last
