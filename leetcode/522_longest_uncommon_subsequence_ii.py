"""
T: O(N**2 * 2**K)
S: O(K)

Brute-force solution which computes every possible subsequence starting from
the largest and compares it to the every word.
"""

import itertools
from typing import List


class Solution:

    def findLUSlength(self, strs: List[str]) -> int:
        strs.sort(key=len, reverse=True)
        max_len = -1
        for i, word in enumerate(strs):
            for subseq in self.get_subseqs(word):
                if max_len >= len(subseq):
                    break
                for j, str_to_check in enumerate(strs):
                    if i == j:
                        continue
                    if self.is_subseq(subseq, str_to_check):
                        break
                else:
                    max_len = max(max_len, len(subseq))
        return max_len

    def get_subseqs(self, word: str):
        for seq_len in reversed(range(1, len(word) + 1)):
            for seq in itertools.combinations(word, seq_len):
                yield seq

    def is_subseq(self, maybe_subseq: List[str], word: str) -> bool:
        read_pointer = 0
        for char in word:
            if char == maybe_subseq[read_pointer]:
                read_pointer += 1
                if read_pointer == len(maybe_subseq):
                    return True
        return False
