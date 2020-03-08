"""
T:
    push O(N)
    pop O(1)
    top O(1)
    empty O(1)
S: O(N)

The only operation that needs to be linear in time is the push.
We convert the queue to a stack every time a new number comes in.
To do that, we have to rotate the queue of length L L-1 times.
"""


import collections


class MyStack:

    def __init__(self):
        self.stack = collections.deque()

    def push(self, x: int) -> None:
        self.stack.append(x)
        self._rotate(len(self.stack)-1)

    def pop(self) -> int:
        return self.stack.popleft()

    def top(self) -> int:
        return self.stack[0]

    def empty(self) -> bool:
        return not self.stack

    def _rotate(self, times: int) -> None:
        for _ in range(times):
            self.stack.append(self.stack.popleft())
