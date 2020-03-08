"""
T: O(N)
S: O(N)

Maintain a set of seen numbers, on each step check the current number against
this set. If current numbers is a double of seen number or double of current
number is in seen - return true. In the end, return false as this means no
doubles were found.
"""

from typing import List, Set


class Solution:

    def checkIfExist(self, arr: List[int]) -> bool:
        seen = set()  # type: Set[int]
        for num in arr:
            if num / 2 in seen or num * 2 in seen:
                return True
            seen.add(num)
        return False
