class Solution(object):
    def subsets(self, nums):
        res = []
        for i in range(1 << len(nums)):
            tmp = []
            for j in range(len(nums)):
                if i & 1 << j:
                    tmp.append(nums[j])
            res.append(tmp)
        return res


"""
0 1 2
000 & (001, 010, 100) => []
001 & (001, 010, 100) => [0]
010 & (001, 010, 100) => [1]
011 & (001, 010, 100) => [0, 1]
100 & (001, 010, 100) => [2]
101 & (001, 010, 100) => [0, 2]
110 & (001, 010, 100) => [1, 2]
111 & (001, 010, 100) => [0, 1, 2]
"""
