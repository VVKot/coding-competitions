class Solution:

    def lastSubstring(self, s: str) -> str:
        N = len(s)
        result = s[-1]
        max_char = s[-1]
        for i in reversed(range(N-1)):
            if s[i] < max_char:
                pass
            elif s[i] > max_char:
                result = s[i:]
                max_char = s[i]
            else:
                result = max(s[i:], result)
        return result
