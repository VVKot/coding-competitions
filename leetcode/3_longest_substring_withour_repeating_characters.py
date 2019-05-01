from typing import Dict


class Solution:

    def lengthOfLongestSubstring(self, s: str) -> int:
        result = 0
        left = 0
        win_char = {}  # type: Dict[str, int]
        for right, curr in enumerate(s):
            if curr in win_char:
                prev_occ = win_char[curr]
                if prev_occ >= left:
                    left = prev_occ + 1
            win_char[curr] = right
            result = max(result, right-left+1)
        return result
