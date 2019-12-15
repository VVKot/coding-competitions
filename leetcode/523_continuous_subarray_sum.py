"""
T: O(N)
S: O(K)

The idea is to find the rolling sum of the sum modulo that we have seen before.
If we find it, this means there is a subarray of sum k*n between the previous
occurrence of this modulo and the current one. We just have to check the
distance between them to eliminate the subarrays of length one, and do not
override the first occurrence of modulo with subsequence ones for the same
reason.
"""

from typing import List


class Solution:

    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        seen_modulos = {0: -1}
        rolling_sum = 0
        for i, num in enumerate(nums):
            rolling_sum += num
            rolling_sum = rolling_sum % k if k != 0 else rolling_sum
            if rolling_sum in seen_modulos:
                if i - seen_modulos[rolling_sum] > 1:
                    return True
            else:
                seen_modulos[rolling_sum] = i
        return False
