class Solution:
    def twoSum(self, nums, limit):
        hash_table = {num: i for i, num in enumerate(nums)}
        for j, curr in enumerate(nums):
            complement = limit-curr
            if complement in hash_table and hash_table[complement] != j:
                return [j, hash_table[complement]]
        return []
