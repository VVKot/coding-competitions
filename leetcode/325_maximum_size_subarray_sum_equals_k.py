"""
T: O(N)
S: O(N)

The trick is to remember previous rolling sums and the current one.
If we have seen current rolling sum minus k previous, that means
there is a subarray of size k in the array. We have to get an index
of a previously seen sum to get a length of the current subarray.
"""


from typing import List


class Solution:

    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        seen_sums = {0: -1}
        rolling_sum = 0
        max_len = 0
        for i, num in enumerate(nums):
            rolling_sum += num
            complement = rolling_sum - k
            if complement in seen_sums:
                max_len = max(max_len, i-seen_sums[complement])
            if rolling_sum not in seen_sums:
                seen_sums[rolling_sum] = i
        return max_len
