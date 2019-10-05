import collections


class Solution:

    def canPermutePalindrome(self, s: str) -> bool:
        input_len = len(s)
        char_count = collections.Counter(s)
        odd_counts_num = sum(count & 1 for count in char_count.values())
        if input_len & 1:
            return odd_counts_num == 1
        return odd_counts_num == 0
