import collections
from typing import Dict, List


class DSU:

    def __init__(self, N: int):
        self.parents = list(range(N))
        self.ranks = [0] * N

    def find(self, node: int) -> int:
        if self.parents[node] == node:
            return node
        self.parents[node] = self.find(self.parents[node])
        return self.parents[node]

    def union(self, n1: int, n2: int) -> None:
        p1, p2 = map(self.find, (n1, n2))
        rank1, rank2 = map(self.ranks.__getitem__, (p1, p2))
        if rank1 >= rank2:
            if rank1 == rank2:
                rank1 += 1
            self.parents[p2] = p1
        else:
            self.parents[p1] = p2


class Solution:

    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        pairs_components = self._get_pairs_components(len(s), pairs)
        connected_components = self._get_connected_components(pairs_components)
        smalest_string = list(s)
        for connected_component in connected_components:
            component_characters = sorted(s[i] for i in connected_component)
            for i, ch in zip(connected_component, component_characters):
                smalest_string[i] = ch
        return ''.join(smalest_string)

    def _get_pairs_components(self,
                              str_len: int,
                              pairs: List[List[int]]) -> List[int]:
        dsu = DSU(str_len)
        for ch1, ch2 in pairs:
            dsu.union(ch1, ch2)
        return [dsu.find(p) for p in dsu.parents]

    def _get_connected_components(self,
                                  components: List[int]) -> List[List[int]]:
        connected_components = \
            collections.defaultdict(list)  # type: Dict[int, List[int]]
        for i, component in enumerate(components):
            connected_components[component].append(i)
        return [sorted(cc) for cc in connected_components.values()]
