class Solution:
    def isToeplitzMatrix(self, matrix):
        if not any(matrix):
            return False
        for y, row in enumerate(matrix):
            for x, val in enumerate(row):
                if y != 0 and x != 0:
                    prev = matrix[y-1][x-1]
                    if prev != val:
                        return False
        return True
