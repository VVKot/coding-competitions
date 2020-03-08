from collections import defaultdict
from typing import List, Dict, Set


class Solution:

    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        adj_dict = defaultdict(set)  # type: Dict[int, Set]
        for s, e in edges:
            adj_dict[s].add(e)
            adj_dict[e].add(s)
        cand = set(range(n))
        while len(cand) > 2:
            leaves = set()
            for i in cand:
                if len(adj_dict[i]) == 1:
                    leaves.add(i)
            for i in leaves:
                cand.remove(i)
                end = list(adj_dict[i])[0]
                del adj_dict[i]
                adj_dict[end].remove(i)
        return list(cand)
