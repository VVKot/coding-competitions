class Solution:

    def validPalindrome(self, s: str) -> bool:
        left, right = 0, len(s)-1
        while left < right:
            if s[left] != s[right]:
                no_left = s[left+1:right+1]
                no_right = s[left:right]
                return self.is_palindrome(no_left) or \
                    self.is_palindrome(no_right)
            left += 1
            right -= 1
        return True

    def is_palindrome(self, s: str) -> bool:
        left, right = 0, len(s)-1
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True
