"""
T: O(N)
S: O(N)

The idea is to flatten the input upfront, after that next and hasNext
become straightforward. To generate the flat list we DFS through the input.
"""

import collections
from typing import Deque, List
"""
This is the interface that allows for creating nested lists.
You should not implement it, or speculate about its implementation
"""


class NestedInteger:

    def isInteger(self) -> bool:
        return True

    def getInteger(self) -> int:
        return 0

    def getList(self) -> List['NestedInteger']:
        return []


class NestedIterator:

    def __init__(self, nestedList: List[NestedInteger]):
        self.processed_elements = collections.deque([])  # type: Deque[int]
        elements_to_process = collections.deque(nestedList)
        while elements_to_process:
            curr = elements_to_process.popleft()
            if curr.isInteger():
                self.processed_elements.append(curr.getInteger())
            else:
                for elem in reversed(curr.getList()):
                    elements_to_process.appendleft(elem)

    def next(self) -> int:
        return self.processed_elements.popleft()

    def hasNext(self) -> bool:
        return bool(self.processed_elements)
