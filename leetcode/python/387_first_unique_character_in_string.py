import collections


class Solution:

    def firstUniqChar(self, s: str) -> int:
        char_counts = collections.Counter(s)
        for i, char in enumerate(s):
            if char_counts[char] == 1:
                return i
        return -1
