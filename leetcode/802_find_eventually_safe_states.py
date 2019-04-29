from collections import defaultdict
from typing import List, Dict, Set


class Solution:

    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        safe = []
        incm = defaultdict(set)  # type: Dict[int, Set[int]]
        out = defaultdict(set)  # type: Dict[int, Set[int]]
        for i, neig in enumerate(graph):
            if not neig:
                safe.append(i)
            for j in neig:
                incm[j].add(i)
                out[i].add(j)
        result = set(safe)
        while safe:
            curr = safe.pop()
            for j in incm[curr]:
                out[j].remove(curr)
                if not out[j]:
                    safe.append(j)
                    result.add(j)
        res = list(result)
        res.sort()
        return res
