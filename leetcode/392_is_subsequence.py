class Solution:

    def isSubsequence(self, s: str, t: str) -> bool:
        haystack = iter(t)
        return all(ch in haystack for ch in s)
