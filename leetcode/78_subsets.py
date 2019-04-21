class Solution(object):
    def subsets(self, nums):
        res = []
        nums.sort()
        #0, 1, 2, 4, 8, 16
        for i in range(1<<len(nums)):# 0b1000 -> base 10 ->8
            tmp = []
            for j in range(len(nums)): # 0, 1, 2
                if i & 1 << j:  # if i 
                    tmp.append(nums[j])
            res.append(tmp)
        return res