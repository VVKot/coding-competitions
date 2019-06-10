from typing import List, Set


class Solution:

    def subarrayBitwiseORs(self, A: List[int]) -> int:
        curr = set()  # type: Set[int]
        result = set()  # type: Set[int]
        for num in A:
            curr = {prev | num for prev in curr} | {num}
            result |= curr
        return len(result)
