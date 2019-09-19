import collections
from typing import List


class Solution:

    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        parents = {num: num for num in nums}
        ranks = {num: 1 for num in nums}

        def find(num):
            return num if parents[num] == num else find(parents[num])

        def union(num1, num2):
            parent1, parent2 = find(num1), find(num2)
            rank1, rank2 = ranks[parent1], ranks[parent2]
            if rank1 >= rank2:
                if rank1 == rank2:
                    ranks[parent1] += 1
                parents[parent2] = parent1
            else:
                parents[parent1] = parent2

        for num in nums:
            if num-1 in parents:
                union(num, num-1)
            if num+1 in nums:
                union(num, num+1)
        return max(collections.Counter([find(p) for p in parents]).values())
ƒ