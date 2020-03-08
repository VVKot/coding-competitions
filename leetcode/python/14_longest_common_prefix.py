from typing import List


class Solution:

    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ""
        if not strs:
            return prefix
        strs.sort()
        for ch1, ch2 in zip(strs[0], strs[-1]):
            if ch1 == ch2:
                prefix += ch1
            else:
                break
        return prefix
