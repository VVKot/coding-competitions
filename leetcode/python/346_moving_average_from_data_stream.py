import collections
from typing import Deque


class MovingAverage:

    def __init__(self, size: int):
        self.window = collections.deque()  # type: Deque[int]
        self.size = size
        self.sum = 0

    def next(self, val: int) -> float:
        self.sum += val
        self.window.append(val)
        if len(self.window) > self.size:
            self.sum -= self.window.popleft()
        return self.sum / len(self.window)
