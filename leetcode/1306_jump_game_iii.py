"""
T: O(N)
S: O(N)

DFS all posibilities to find if there is an answer. Use visited set to track
seen elements.
"""

from typing import List, Set


class Solution:

    def canReach(self, arr: List[int], start: int) -> bool:
        visited = set()  # type: Set[int]
        stack = [start]
        while stack:
            curr = stack.pop()
            if not 0 <= curr < len(arr):
                continue
            if arr[curr] == 0:
                return True
            if curr in visited:
                continue
            visited.add(curr)
            stack.append(curr - arr[curr])
            stack.append(curr + arr[curr])
        return False
