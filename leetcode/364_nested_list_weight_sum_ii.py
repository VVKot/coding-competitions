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

    def depthSumInverse(self, nestedList: List[NestedInteger]) -> int:
        unweighted = weighted = 0
        while nestedList:
            unweighted += sum([x.getInteger() for x in nestedList
                               if x.isInteger()])
            nestedList = sum([x.getList() for x in nestedList
                              if not x.isInteger()], [])
            weighted += unweighted
        return weighted
