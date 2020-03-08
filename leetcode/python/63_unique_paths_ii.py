"""
T: O(R*C)
S: O(1)

The 1D DP solution is easy, the trick is to figure out in-place one.
If you fill in the first row and column correctly - after that you
have to just iterate through matrix and sum up top and left values.
"""


from typing import List


class Solution:

    EMPTY, OBSTACLE = range(2)

    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if not any(obstacleGrid) or obstacleGrid[0][0] == self.OBSTACLE:
            return 0
        obstacleGrid[0][0] = 1
        self.rows = len(obstacleGrid)
        self.cols = len(obstacleGrid[0])
        self.fill_first_column(obstacleGrid)
        self.fill_first_row(obstacleGrid)
        self.calculate_paths_number(obstacleGrid)
        return obstacleGrid[-1][-1]

    def calculate_paths_number(self, obstacleGrid):
        for y in range(1, self.rows):
            for x in range(1, self.cols):
                if obstacleGrid[y][x] == self.OBSTACLE:
                    obstacleGrid[y][x] = 0
                else:
                    left = obstacleGrid[y][x-1]
                    top = obstacleGrid[y-1][x]
                    obstacleGrid[y][x] = left + top

    def fill_first_row(self, obstacleGrid):
        for x in range(1, self.cols):
            obstacleGrid[0][x] = int(obstacleGrid[0][x] == self.EMPTY and
                                     obstacleGrid[0][x-1] == 1)

    def fill_first_column(self, obstacleGrid):
        for y in range(1, self.rows):
            obstacleGrid[y][0] = int(obstacleGrid[y][0] == self.EMPTY and
                                     obstacleGrid[y-1][0] == 1)
