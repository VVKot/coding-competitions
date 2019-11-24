"""
T: O(N**2)
S: O(N)

Just do as they say. Making a list is more efficient than
performing substring every time.
"""


from typing import List


class Solution:

    PLUS, MINUS = '+', '-'

    def generatePossibleNextMoves(self, s: str) -> List[str]:
        N = len(s)
        chars = list(s)
        possible_next_states = []
        for i in range(0, N-1):
            if chars[i] == chars[i+1] == self.PLUS:
                chars[i] = chars[i+1] = self.MINUS
                possible_next_states.append(''.join(chars))
                chars[i] = chars[i+1] = self.PLUS
        return possible_next_states
