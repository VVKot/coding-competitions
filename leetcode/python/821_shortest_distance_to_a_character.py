from typing import List
from sys import maxsize


class Solution:

    def shortestToChar(self, S: str, C: str) -> List[int]:
        N = len(S)
        result = [maxsize] * N
        prev = None
        for i in range(N):
            if S[i] == C:
                prev = i
                result[i] = 0
            elif prev is not None:
                result[i] = i - prev
        prev = None
        for i in range(N-1, -1, -1):
            if S[i] == C:
                prev = i
            elif prev is not None:
                result[i] = min(result[i], prev - i)
        return result
