class Solution:
    def maximumGap(self, nums):
        if not nums:
            return 0

        max_num = max(nums)
        buckets = [[] for _ in range(10)]
        exp = 1
        while max_num / exp > 0:
            for num in nums:
                buckets[int((num/exp) % 10)].append(num)
            nums = []
            for bucket in buckets:
                nums.extend(bucket)
            buckets = [[] for i in range(10)]
            exp *= 10

        max_gap = 0
        for i in range(1, len(nums)):
            max_gap = max(max_gap, nums[i]-nums[i-1])
        return max_gap
