from typing import List


class Solution:

    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        answer = [[10000 * x for x in row] for row in matrix]
        for _ in range(4):
            for row in answer:
                for j in range(1, len(row)):
                    row[j] = min(row[j], row[j-1] + 1)
            answer = list(map(list, zip(*answer[::-1])))
        return answer
