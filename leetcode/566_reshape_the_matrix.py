from typing import List


class Solution:
    def matrixReshape(self,
                      nums: List[List[int]],
                      r: int,
                      c: int) -> List[List[int]]:
        rows = len(nums)
        cols = len(nums[0])
        if rows * cols != r * c:
            return nums
        result = []  # type: List[List[int]]
        for y in range(r):
            result.append([])
            for x in range(c):
                index = y * c + x
                val = nums[index // cols][index % cols]
                result[y].append(val)
        return result
