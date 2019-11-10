"""
T: O(N)
S: O(1) (additional)

First, place values for all columns with a column sum == 2.
After that, we can greedily place remaining ones to any row.
"""


from typing import List


class Solution:

    INVALID_INPUT_RESULT = []  # type: List[List[int]]
    VALUE = 1

    def reconstructMatrix(self,
                          upper: int,
                          lower: int,
                          colsum: List[int]) -> List[List[int]]:
        if sum(colsum) != upper + lower:
            return self.INVALID_INPUT_RESULT
        M = self._get_default_matrix(colsum)
        try:
            for i, curr_sum in enumerate(colsum):
                if curr_sum == 2:
                    upper = self._try_place_value(M[0], i, upper)
                    lower = self._try_place_value(M[1], i, lower)
            for i, curr_sum in enumerate(colsum):
                if curr_sum == 1:
                    if upper:
                        upper = self._try_place_value(M[0], i, upper)
                    else:
                        lower = self._try_place_value(M[1], i, lower)
        except ValueError:
            return self.INVALID_INPUT_RESULT
        return M

    def _get_default_matrix(self, colsum: List[int]) -> List[List[int]]:
        N = len(colsum)
        return [[0 for _ in range(N)] for _ in range(2)]

    def _try_place_value(self,
                         row: List[int],
                         position: int,
                         value_count: int) -> int:
        if value_count:
            row[position] = self.VALUE
            return value_count - 1
        raise ValueError()
