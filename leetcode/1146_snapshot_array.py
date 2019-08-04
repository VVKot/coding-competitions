import copy
import collections
from typing import Dict, DefaultDict


class SnapshotArray:

    def __init__(self, length: int):
        self.array = collections.defaultdict(
            int)  # type: DefaultDict[int, int]
        self.store = {}  # type: Dict[int, DefaultDict[int, int]]
        self.time = 0

    def set(self, index: int, val: int) -> None:
        self.array[index] = val

    def snap(self) -> int:
        self.store[self.time] = copy.deepcopy(self.array)
        self.time += 1
        return self.time - 1

    def get(self, index: int, snap_id: int) -> int:
        return self.store[snap_id][index]
