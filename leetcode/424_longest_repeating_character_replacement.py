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
        left = 0
        total_count = max_count = 0
        max_str_len = 0
        ch_count = collections.Counter()  # type: Counter[str]
        for right, ch in enumerate(s):
            ch_count[ch] += 1
            total_count += 1
            max_count = max(max_count, ch_count[ch])
            if total_count - max_count > k:
                ch_count[s[left]] -= 1
                total_count -= 1
                left += 1
            max_str_len = max(max_str_len, right - left + 1)
        return max_str_len
