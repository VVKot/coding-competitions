import heapq
from typing import List


class DinnerPlates:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.stacks = []  # type: List[List[int]]
        self.push_indices = []  # type: List[int]

    def push(self, val: int) -> None:
        if self.push_indices:
            push_index = heapq.heappop(self.push_indices)
            if push_index < len(self.stacks):
                return self.stacks[push_index].append(val)
            self.push_indices = []

        if self.stacks and len(self.stacks[-1]) < self.cap:
            return self.stacks[-1].append(val)
        self.stacks.append([val])

    def pop(self) -> int:
        while self.stacks and not self.stacks[-1]:
            self.stacks.pop()
        if self.stacks:
            return self.stacks[-1].pop()
        return -1

    def popAtStack(self, index: int) -> int:
        if not self.stacks or not self.stacks[index]:
            return -1
        heapq.heappush(self.push_indices, index)
        return self.stacks[index].pop()
