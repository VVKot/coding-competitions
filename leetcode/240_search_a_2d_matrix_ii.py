from typing import List


class Solution:

    def searchMatrix(self, matrix: List[List[int]], target: int) -> int:
        if not any(matrix):
            return False
        rows = len(matrix)
        cols = len(matrix[0])
        y, x = 0, cols-1
        while x >= 0 and y < rows:
            curr_number = matrix[y][x]
            if curr_number == target:
                return True
            if curr_number > target:
                x -= 1
            else:
                y += 1
        return False
