"""
T: O(N)
S: O(N)

The classical sliding-window question, here we iterate over the string and
store count of each character. If adding a new character makes us unable to
expand the window, we move the window to the right. There is no need to reset
the count of maximum occurences since we are only interested in the all-time
maximum.

"""

import collections
from typing import Counter


class Solution:

    def characterReplacement(self, s: str, k: int) -> int:
        char_count = collections.Counter()  # type: Counter[str]
        max_count = 0
        left = 0
        for right, char in enumerate(s):
            char_count[char] += 1
            max_count = max(max_count, char_count[char])
            current_len = right - left + 1
            if current_len - max_count > k:
                char_count[s[left]] -= 1
                left += 1
        return len(s) - left
