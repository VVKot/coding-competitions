"""
T: O(N)
S: O(N)

We use a stack to store previous scores. That's it!
"""

from typing import List


class Solution:

    def calPoints(self, ops: List[str]) -> int:
        scores = []  # type: List[int]
        for op in ops:
            if op == '+':
                score = sum(scores[-2:])
                scores.append(score)
            elif op == 'D':
                score = scores[-1] * 2
                scores.append(score)
            elif op == 'C':
                scores.pop()
            else:
                score = int(op)
                scores.append(score)
        return sum(scores)
