from typing import List


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        min_num, max_num = min(nums), max(nums)
        buckets = [0] * (max_num - min_num + 1)
        for num in nums:
            buckets[num - min_num] += 1
        return [i + min_num
                for i, count in enumerate(buckets)
                for _ in range(count)]
