class Solution(object):
    def maxIncreaseKeepingSkyline(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        result = 0
        grid_length = len(grid)
        top_skyline = [-1] * grid_length
        left_skyline = [-1] * grid_length
        for j, row in enumerate(grid):
            for i, elem in enumerate(row):
                if elem > top_skyline[i]:
                    top_skyline[i] = elem
                if elem > left_skyline[j]:
                    left_skyline[j] = elem
        for j, row in enumerate(grid):
            for i, elem in enumerate(row):
                diff = min(top_skyline[i], left_skyline[j]) - elem
                if diff > 0:
                  result += diff
        return result