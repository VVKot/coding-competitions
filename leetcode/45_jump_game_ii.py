class Solution:
    def jump(self, nums):
        dest = len(nums) - 1
        result = 0
        i = 0
        while i < dest:
            result += 1
            num = nums[i]
            if dest - i <= num:
                return result
            max_ = 0
            next_idx = 0
            for j in range(i+1, i+num+1):
                curr = j + nums[j]
                if curr > max_:
                    max_ = curr
                    next_idx = j
            i = next_idx
        return result
