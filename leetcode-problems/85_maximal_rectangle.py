class Solution:
    def maximalRectangle(self, matrix):
        if not any(matrix):
            return 0
        N = len(matrix[0])
        heights = [0] * (N + 1)
        result = 0
        for row in matrix:
            for i in range(N):
                heights[i] = heights[i] + 1 if row[i] == '1' else 0
            height_indices = [-1]
            for i in range(N + 1):
                while heights[i] < heights[height_indices[-1]]:
                    h = heights[height_indices.pop()]
                    w = i - 1 - height_indices[-1]
                    result = max(result, h * w)
                height_indices.append(i)
        return result
