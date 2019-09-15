from typing import List


class Solution:

    MAX_SUM = 10**9 + 7

    def kConcatenationMaxSum(self, arr: List[int], k: int) -> int:
        result = 0
        if all(i <= 0 for i in arr):
            return result

        max_subarray_sum = curr = 0
        for num in arr:
            if curr + num > 0:
                curr += num
                max_subarray_sum = max(max_subarray_sum, curr)
            else:
                curr = 0

        array_sum = sum(arr)
        all_arrays_sum = array_sum * k

        if k == 1:
            return max(max_subarray_sum, all_arrays_sum) % self.MAX_SUM

        max_left_prefix = max_right_prefix = 0
        curr_left = curr_right = 0
        N = len(arr)
        for num in arr:
            curr_left += num
            max_left_prefix = max(max_left_prefix, curr_left)
        for num in reversed(arr):
            curr_right += num
            max_right_prefix = max(max_right_prefix, curr_right)

        max_with_prefix = max_left_prefix + \
            max_right_prefix + max(array_sum * (k-2), 0)

        return max([max_subarray_sum,
                    all_arrays_sum,
                    max_with_prefix]) % self.MAX_SUM
