from typing import List


class Solution:

    def longestConsecutive(self, nums: List[int]) -> int:
        longest_seq_len = 0
        if not nums:
            return longest_seq_len
        available_nums = set(nums)
        for num in nums:
            if num-1 not in available_nums:
                curr_seq_len = 1
                curr = num
                while curr+1 in available_nums:
                    curr += 1
                    curr_seq_len += 1
                longest_seq_len = max(longest_seq_len, curr_seq_len)
        return longest_seq_len
