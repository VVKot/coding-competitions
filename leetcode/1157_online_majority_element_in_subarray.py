import bisect
import collections
from typing import DefaultDict, List


class MajorityChecker:

    def __init__(self, arr: List[int]):
        self.num_map = \
            collections.defaultdict(list)  # type: DefaultDict[int, List[int]]
        for i, num in enumerate(arr):
            self.num_map[num].append(i)

    def query(self, left: int, right: int, threshold: int) -> int:
        for num, occs in self.num_map.items():
            N = len(occs)
            if N < threshold:
                continue
            occ_left = min(bisect.bisect_left(occs, left), N-1)
            occ_right = min(bisect.bisect_left(occs, right), N-1)
            total_occs = occ_right - occ_left + 1
            if occ_right == N or occs[occ_right] > right:
                total_occs -= 1
            if total_occs >= threshold:
                return num
        return -1
