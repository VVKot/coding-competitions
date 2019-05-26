from typing import List


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        result = []
        visited = [False] * len(nums)

        def backtrack(curr, rest, seen):
            if len(curr) == len(rest):
                result.append(curr)
            else:
                for i, num in enumerate(rest):
                    if seen[i]:
                        continue
                    if i > 0 and rest[i-1] == num and not seen[i-1]:
                        continue
                    seen[i] = True
                    backtrack(curr + [num], rest, seen)
                    seen[i] = False
        nums.sort()
        backtrack([], nums, visited)
        return result
