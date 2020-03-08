"""
T: O(A + B)
S: O(A + B)

The words we are looking for are only present once across both sequences. Count
the words and find those that are unique.
"""

import collections
from typing import List


class Solution:

    def uncommonFromSentences(self, A: str, B: str) -> List[str]:
        all_words = collections.Counter(A.split()) + \
            collections.Counter(B.split())
        return [word for word, count in all_words.items() if count == 1]
