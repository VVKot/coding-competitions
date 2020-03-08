from typing import Set


class Solution:

    def lengthOfLongestSubstring(self, s: str) -> int:
        result = 0
        left = 0
        substring = set()  # type: Set[str]
        for right, ch in enumerate(s):
            if ch in substring:
                while ch in substring:
                    substring.remove(s[left])
                    left += 1
            substring.add(ch)
            result = max(result, right-left+1)
        return result
