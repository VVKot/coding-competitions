class Solution(object):

    def get_tl(self, matrix, y, x):
        result = []
        for r, c in [(y-1, x), (y, x-1), (y-1, x-1)]:
            if r >= 0 and c >= 0:
                curr = matrix[r][c]
                result.append(curr)
            else:
                result.append(0)
        return result

    def maximalSquare(self, matrix):
        result = 0
        for y, row in enumerate(matrix):
            for x, num in enumerate(row):
                matrix[y][x] = int(num)
        for y, row in enumerate(matrix):
            for x, num in enumerate(row):
                if not num:
                    continue
                curr = num
                top, left, top_left = self.get_tl(matrix, y, x)
                curr = min(top, left, top_left) + 1
                matrix[y][x] = curr
                result = max(result, curr)
