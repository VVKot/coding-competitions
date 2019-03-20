class Solution:
	def twoSum(self, nums, limit):
		hash_table = {}
		for j, curr in enumerate(nums):
			complement = limit-curr
			if complement in hash_table and hash_table[complement] != j:
				return sorted([j, hash_table[complement]])
			hash_table[curr] = j
		return []
