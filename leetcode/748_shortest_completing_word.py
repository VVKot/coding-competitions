from typing import List, Dict
from collections import defaultdict


class Solution:

    def shortestCompletingWord(self,
                               licensePlate: str,
                               words: List[str]) -> str:
        lp_count, result = defaultdict(int), ""  # type: Dict[str, int], str
        for char in licensePlate:
            if char.isalpha():
                lp_count[char.lower()] += 1
        for word in words:
            word_count = dict(lp_count)
            for char in word.lower():
                if char in word_count:
                    word_count[char] -= 1
                    if not word_count[char]:
                        del word_count[char]
            if not word_count and (not result or len(word) < len(result)):
                result = word
        return result
