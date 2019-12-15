"""
T: O(N)
S: O(N)

The idea is to flatten the input upfront, after that next and hasNext
become straightforward. To generate the flat list we DFS through the input.
"""

import collections
from typing import List, Union
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
        self.flat_list = collections.deque(
            [])  # type: Union(NestedInteger, List[NestedInteger])
        to_parse = collections.deque(nestedList)
        while to_parse:
            curr = to_parse.popleft()
            if curr.isInteger():
                self.flat_list.append(curr.getInteger())
            for list_item in reversed(curr.getList()):
                to_parse.appendleft(list_item)

    def next(self) -> int:
        return self.flat_list.popleft()

    def hasNext(self) -> bool:
        return len(self.flat_list) != 0


# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())
