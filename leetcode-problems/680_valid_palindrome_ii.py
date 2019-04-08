class Solution:
    def validPalindrome(self, s):
        left, right = 0, len(s) - 1
        while left < right:
            if s[left] != s[right]:
                no_right, no_left = s[left:right], s[left + 1:right + 1]
                return no_right == no_right[::-1] or no_left == no_left[::-1]
            left, right = left + 1, right - 1
        return True
