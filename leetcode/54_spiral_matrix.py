from typing import Generator, List, Tuple


class Solution:

    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        order = []  # type: List[int]
        if not matrix:
            return order
        y1, x1, y2, x2 = 0, 0, len(matrix)-1, len(matrix[0])-1
        while y1 <= y2 and x1 <= x2:
            for y, x in self.get_nodes_in_spiral(y1, x1, y2, x2):
                order.append(matrix[y][x])
            y1 += 1
            y2 -= 1
            x1 += 1
            x2 -= 1
        return order

    def get_nodes_in_spiral(self,
                            y1: int,
                            x1: int,
                            y2: int,
                            x2: int) -> Generator[Tuple[int, int], None, None]:
        for x in range(x1, x2+1):
            yield y1, x
        for y in range(y1+1, y2+1):
            yield y, x2
        if y1 < y2 and x1 < x2:
            for x in reversed(range(x1+1, x2)):
                yield y2, x
            for y in reversed(range(y1+1, y2+1)):
                yield y, x1
