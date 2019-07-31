class Solution:

    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0
        H = len(haystack)
        N = len(needle)
        for i in range(H-N+1):
            for j in range(i, i+N):
                if haystack[j] != needle[j-i]:
                    break
            else:
                return i
        return -1
