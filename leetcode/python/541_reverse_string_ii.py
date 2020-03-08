from typing import List


class Solution:

    def reverseStr(self, s: str, k: int) -> str:
        chars = list(s)
        N = len(chars)
        for start in range(0, N, 2*k):
            end = min(start + k, N) - 1
            self.reverse_elements(chars, start, end)
        return ''.join(chars)

    def reverse_elements(self, seq: List[str], start: int, end: int):
        while start < end:
            seq[start], seq[end] = seq[end], seq[start]
            start += 1
            end -= 1
