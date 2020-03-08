"""
T: O(N)
S: O(1) - not counting output space

Find the overall pattern - how many of each character do we have to have in a
word for it to be universal. After that just check every word again pattern.
"""

import collections
from typing import Counter, List


class Solution:

    def wordSubsets(self, A: List[str], B: List[str]) -> List[str]:
        pattern = self.get_pattern(B)
        return [word for word in A if not pattern - collections.Counter(word)]

    def get_pattern(self, B: List[str]) -> Counter[str]:
        pattern = collections.Counter()  # type: Counter[str]
        for word in B:
            curr = collections.Counter(word)
            for letter, count in curr.items():
                pattern[letter] = max(pattern[letter], count)
        return pattern
