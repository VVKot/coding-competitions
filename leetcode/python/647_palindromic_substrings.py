class Solution:

    def countSubstrings(self, s: str) -> int:
        substr_count = 0
        N = len(s)
        substr_count += N
        for substr_len in range(2, N+1):
            for i in range(0, N-substr_len+1):
                if self.is_palindrome(s[i:i+substr_len]):
                    substr_count += 1
        return substr_count

    def is_palindrome(self, s: str) -> bool:
        return s == s[::-1]
