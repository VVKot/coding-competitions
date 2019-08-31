import collections
from typing import Counter, List


class Solution:

    def wordSubsets(self, A: List[str], B: List[str]) -> List[str]:
        pattern = self.get_pattern(B)
        return [a for a in A if not pattern - collections.Counter(a)]

    def get_pattern(self, B: List[str]) -> Counter[str]:
        pattern = collections.Counter()  # type: Counter[str]
        unique_patterns = set(B)
        for p in unique_patterns:
            curr = collections.Counter(p)
            for letter, count in curr.items():
                pattern[letter] = max(pattern[letter], count)
        return pattern
