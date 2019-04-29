from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not any(matrix):
            return False
        rows = len(matrix)
        cols = len(matrix[0])
        left = 0
        right = rows-1
        target_row = None
        while left <= right:
            mid = (left + right) // 2
            mid_start = matrix[mid][0]
            mid_end = matrix[mid][-1]
            if mid_start <= target <= mid_end:
                target_row = mid
                break
            if target > mid_end:
                left = mid + 1
            else:
                right = mid - 1
        if target_row is None:
            return False
        left = 0
        right = cols - 1
        while left <= right:
            mid = (left + right) // 2
            at_mid = matrix[target_row][mid]
            if at_mid == target:
                return True
            if at_mid < target:
                left = mid + 1
            else:
                right = mid - 1
        return False
