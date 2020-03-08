from typing import List

"""
This is the interface that allows for creating nested lists.
You should not implement it, or speculate about its implementation
"""


class NestedInteger:

    def __init__(self, value=None):
        pass

    def isInteger(self):
        pass

    def add(self, elem):
        pass

    def setInteger(self, value):
        pass

    def getInteger(self):
        pass

    def getList(self):
        pass


class Solution:

    def depthSum(self, nestedList: List[NestedInteger]) -> int:
        result, depth = 0, 1
        while nestedList:
            result += depth * sum([x.getInteger() for x in nestedList
                                   if x.isInteger()])
            nestedList = sum([x.getList() for x in nestedList
                              if not x.isInteger()], [])
            depth += 1
        return result
