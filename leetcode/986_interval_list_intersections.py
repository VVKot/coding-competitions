from typing import List


class Solution:
    def intervalIntersection(self,
                             A: List[List[int]],
                             B: List[List[int]]) -> List[List[int]]:
        result = []  # type: List[List[int]]
        if not A or not B:
            return result
        i = j = 0
        a, b = len(A), len(B)
        while i < a and j < b:
            intA = A[i]
            intB = B[j]
            start = max(intA[0], intB[0])
            end = min(intA[1], intB[1])
            if start <= end:
                result.append([start, end])
            if intA[1] < intB[1]:
                i += 1
            else:
                j += 1
        return result
