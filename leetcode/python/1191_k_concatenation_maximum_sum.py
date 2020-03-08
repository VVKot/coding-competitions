from typing import List


class Solution:

    MAX_SUM = 10**9 + 7

    def kConcatenationMaxSum(self, arr: List[int], k: int) -> int:
        max_subarray_sum = self._get_max_subarray_sum(arr)
        array_sum = sum(arr)
        if k == 1:
            return max(max_subarray_sum,
                       array_sum) % self.MAX_SUM

        total_concatendated_sum = array_sum * k
        max_overlapped_subarray_sum = self._get_max_subarray_sum(arr + arr)
        max_overlapped_subarray_sum += max(0, array_sum * (k-2))

        return max([max_subarray_sum,
                    total_concatendated_sum,
                    max_overlapped_subarray_sum]) % self.MAX_SUM

    def _get_max_subarray_sum(self, nums: List) -> int:
        max_sum = curr_sum = 0
        for num in nums:
            curr_sum += num
            if curr_sum > 0:
                max_sum = max(max_sum, curr_sum)
            else:
                curr_sum = 0
        return max_sum
