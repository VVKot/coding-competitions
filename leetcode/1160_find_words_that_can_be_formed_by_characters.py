import collections
from typing import List


class Solution:

    def countCharacters(self, words: List[str], chars: str) -> int:
        good = collections.Counter(chars)
        result = 0
        for word in words:
            missing = collections.Counter(word) - good
            if not missing:
                result += len(word)
        return result
