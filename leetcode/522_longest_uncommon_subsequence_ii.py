"""
T: O(N**2 * K)
S: O(1)

Brute-force solution which computes every possible subsequence starting from
the largest and compares it to the every word.
"""

from typing import List


class Solution:

    def findLUSlength(self, strs: List[str]) -> int:
        strs.sort(key=len, reverse=True)
        for i, subseq in enumerate(strs):
            is_subseq_of_any = False
            for j, word in enumerate(strs):
                if i == j:
                    continue
                if len(word) < len(subseq):
                    break
                if self.is_subseq(subseq, word):
                    is_subseq_of_any = True
                    break
            if not is_subseq_of_any:
                return len(subseq)
        return -1

    def is_subseq(self, subseq: str, word: str) -> bool:
        i = j = 0
        while i < len(subseq) and j < len(word):
            if subseq[i] == word[j]:
                i += 1
            j += 1
        return i == len(subseq)
