class Solution:
    def threeSum(self, nums):
        if len(nums) < 3:
            return []
        nums.sort()
        result = set()
        for i, low in enumerate(nums[:-2]):
            if low > 0:
                break
            if i >= 1 and low == nums[i-1]:
                continue
            complement_pair = set()
            for high in nums[i+1:]:
                mid = -low-high
                if high not in complement_pair:
                    complement_pair.add(mid)
                else:
                    result.add((low, mid, high))
        return list(map(list, result))
