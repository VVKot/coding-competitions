from typing import List
from sys import maxsize as maxint


class Solution:

    def minDistance(self,
                    height: int,
                    width: int,
                    tree: List[int],
                    squirrel: List[int],
                    nuts: List[List[int]]) -> int:
        total_distance = 0
        max_saved = -maxint-1
        for nut in nuts:
            tree_distance = self.get_distance(tree, nut)
            total_distance += tree_distance
            squirrel_distance = self.get_distance(squirrel, nut)
            curr_saved = tree_distance - squirrel_distance
            max_saved = max(max_saved, curr_saved)
        return total_distance * 2 - max_saved

    def get_distance(self, src: List[int], dst: List[int]) -> int:
        y1, x1 = src
        y2, x2 = dst
        return abs(y2-y1) + abs(x2-x1)
