"""
T: O(N)
S: O(1)

A classical problem for applying sliding window technique.
Linear time memory solution is easy.
To get a constant time one we have to use two pointers.
One neat optimization - no need to store current count of the last seen char.
We can calculate it later from the position of character and the current one.
"""
from typing import List


class Solution:

    def compress(self, chars: List[str]) -> int:
        anchor = write = 0
        N = len(chars)
        for read in range(N):
            if read == N-1 or chars[read] != chars[read+1]:
                chars[write] = chars[anchor]
                write += 1
                if read > anchor:
                    for digit in str(read-anchor+1):
                        chars[write] = digit
                        write += 1
                anchor = read+1
        return write
