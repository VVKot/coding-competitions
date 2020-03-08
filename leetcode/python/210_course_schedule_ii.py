import collections
from typing import List, Set, DefaultDict


class Solution:

    def findOrder(self,
                  numCourses: int,
                  prerequisites: List[List[int]]) -> List[int]:
        pre_count = self.get_prereq_count(numCourses, prerequisites)
        opens = self.get_opened(prerequisites)
        order = []
        to_study = [c for c in range(numCourses) if pre_count[c] == 0]
        while to_study:
            curr = to_study.pop()
            order.append(curr)
            for opened in opens[curr]:
                pre_count[opened] -= 1
                if not pre_count[opened]:
                    to_study.append(opened)
        return [] if len(order) < numCourses else order

    def get_prereq_count(self,
                         numCourses: int,
                         edges: List[List[int]]) -> List[int]:
        pre_count = [0] * numCourses
        for course, pre in edges:
            pre_count[course] += 1
        return pre_count

    def get_opened(self,
                   edges: List[List[int]]) -> DefaultDict[int, Set[int]]:
        opens = \
            collections.defaultdict(set)  # type: DefaultDict[int, Set[int]]
        for course, pre in edges:
            opens[pre].add(course)
        return opens
