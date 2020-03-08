from typing import List


class Solution:

    def shortestDistance(self, words: List[str], word1: str, word2: str) -> int:
        word1_idx, word2_idx = -1, -1
        min_dist = float('inf')
        for i, word in enumerate(words):
            if word == word1:
                word1_idx = i
            if word == word2:
                word2_idx = i

            if word1_idx != -1 and word2_idx != -1:
                min_dist = min(min_dist, abs(word1_idx - word2_idx))
        return min_dist
