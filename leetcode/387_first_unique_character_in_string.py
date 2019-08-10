import collections
from typing import Counter


class Solution:

    def firstUniqChar(self, s: str) -> int:
        char_positions = {}
        char_count = collections.Counter()  # type: Counter[str]
        for i, char in enumerate(s):
            char_count[char] += 1
            if char_count[char] == 1:
                char_positions[char] = i
        for char, count in char_count.items():
            if count == 1:
                return char_positions[char]
        return -1
