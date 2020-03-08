"""
T: O(N)
S: O(1)

For each number, calculate the maximum possible sum
that can be achieved at its value modulo every number from 0 to divisor-1.
The maximum sum which modulo divisor is 0 is the sum we are looking for.
"""


from typing import List


class Solution:

    DIVISOR = 3

    def maxSumDivThree(self, nums: List[int]) -> int:
        max_mod_sums = [0 for _ in range(self.DIVISOR)]
        for num in nums:
            for prev in max_mod_sums[:]:
                curr_sum = num + prev
                mod = curr_sum % self.DIVISOR
                max_mod_sums[mod] = max(max_mod_sums[mod], curr_sum)
        return max_mod_sums[0]
