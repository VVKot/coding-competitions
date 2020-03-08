from typing import List


class Solution:

    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0
        suffix_prefix = self._get_kmp_table(needle)
        H, N = len(haystack), len(needle)
        i = j = 0
        while i < H and j < N:
            if haystack[i] == needle[j]:
                j += 1
                i += 1
            else:
                if j:
                    j = suffix_prefix[j-1]
                else:
                    i += 1
        return i - j if j == N else -1

    def _get_kmp_table(self, needle: str) -> List[int]:
        N = len(needle)
        kmp = [0] * N
        j = 0
        i = 1
        while i < N:
            if needle[i] == needle[j]:
                j += 1
                kmp[i] = j
                i += 1
            else:
                if j == 0:
                    i += 1
                else:
                    j = kmp[j-1]
        return kmp
