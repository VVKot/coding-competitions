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
        cells = [num for row in nums for num in row]
        result = []
        for i in range(r):
            left, right = i*c, (i+1)*c
            result.append(cells[left:right])
        return result
