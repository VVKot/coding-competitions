class Solution(object):

    def get_pali_len(self, s, left, right):
        s_len = len(s)
        result = 0, 0
        while left >= 0 and right < s_len:
            if s[left] == s[right]:
                result = left, right
                left -= 1
                right += 1
            else:
                break
        return result

    def longestPalindrome(self, s):
        result = (0, 0)
        for i in range(len(s)):
            left, right = 0, 0
            left1, right1 = self.get_pali_len(s, i-1, i+1)
            left2, right2 = self.get_pali_len(s, i, i+1)
            if right1-left1 > right2-left2:
                left, right = left1, right1
            else:
                left, right = left2, right2
            if right-left > result[1]-result[0]:
                result = left, right
        return s[result[0]:result[1]+1]
