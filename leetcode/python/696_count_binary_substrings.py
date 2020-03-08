class Solution:

    def countBinarySubstrings(self, s: str) -> int:
        prev_running_len, curr_running_len = 0, 1
        result = 0
        for i in range(1, len(s)):
            if s[i - 1] == s[i]:
                curr_running_len += 1
            else:
                prev_running_len = curr_running_len
                curr_running_len = 1
            if prev_running_len >= curr_running_len:
                result += 1
        return result
