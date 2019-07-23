import collections
from typing import List, Set, Deque, Tuple, DefaultDict


class Solution:

    def shortestAlternatingPaths(self,
                                 n: int,
                                 red_edges: List[List[int]],
                                 blue_edges: List[List[int]]) -> List[int]:
        result = [0] + [-1] * (n-1)
        red = collections.defaultdict(set)  # type: DefaultDict[int, Set[int]]
        blue = collections.defaultdict(set)  # type: DefaultDict[int, Set[int]]
        for src, dst in red_edges:
            red[src].add(dst)
        for src, dst in blue_edges:
            blue[src].add(dst)
        for i in range(1, n):
            q = collections.deque([])  # type: Deque[Tuple[int, int, bool]]
            for el in red[0]:
                q.append((el, 1, True))
            for el in blue[0]:
                q.append((el, 1, False))
            blue_vis = set()  # type: Set[int]
            red_vis = set()  # type: Set[int]
            while q:
                curr, path_len, is_red = q.popleft()
                if curr == i:
                    result[i] = path_len
                    break
                if is_red:
                    if curr in red_vis:
                        continue
                    red_vis.add(curr)
                    for el in blue[curr]:
                        q.append((el, path_len+1, False))
                else:
                    if curr in blue_vis:
                        continue
                    blue_vis.add(curr)
                    for el in red[curr]:
                        q.append((el, path_len+1, True))
        return result
