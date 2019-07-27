import collections
from typing import List, DefaultDict


class Solution:

    def minimumSemesters(self, N: int, relations: List[List[int]]) -> int:
        deps_count = [0] * N
        unlocks = \
            collections.defaultdict(list)  # type: DefaultDict[int, List[int]]
        for pre, end in relations:
            deps_count[end-1] += 1
            unlocks[pre-1].append(end-1)
        result = 0
        stack = [i for i, val in enumerate(deps_count) if not val]
        visited = set()
        while stack:
            for j in stack:
                visited.add(j)
                for un in unlocks[j]:
                    deps_count[un] -= 1
            result += 1
            stack = [i for i, val in enumerate(
                deps_count) if not val and i not in visited]
        if len(visited) == N:
            return result
        return -1
