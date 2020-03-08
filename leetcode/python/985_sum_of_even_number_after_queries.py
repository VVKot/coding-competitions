from typing import List


class Solution:

    def sumEvenAfterQueries(self,
                            A: List[int],
                            queries: List[List[int]]) -> List[int]:
        even_sum = sum(num for num in A if not num & 1)
        result = []
        for val, idx in queries:
            if not A[idx] & 1:
                even_sum -= A[idx]
            A[idx] += val
            if not A[idx] & 1:
                even_sum += A[idx]
            result.append(even_sum)
        return result
