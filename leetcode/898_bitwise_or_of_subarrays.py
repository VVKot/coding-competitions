"""
T: O(N * logW), where W is the maximum size of the element in the list
S: O(N * logW)

Find all possible elements for the current iteration based on the result of the
previous iteration. There can not be more of those than logW because for the
new element to be added it has to have more 1's in its binary representation.
"""

from typing import List, Set


class Solution:

    def subarrayBitwiseORs(self, A: List[int]) -> int:
        curr = set()  # type: Set[int]
        result = set()  # type: Set[int]
        for num in A:
            curr = {prev | num for prev in curr} | {num}
            result |= curr
        return len(result)
