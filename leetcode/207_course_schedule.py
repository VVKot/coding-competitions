import collections
from typing import List, DefaultDict


class Solution:

    def canFinish(self,
                  numCourses: int,
                  prerequisites: List[List[int]]) -> bool:
        num_prereq = [0 for _ in range(numCourses)]
        opens_courses = \
            collections.defaultdict(list)  # type: DefaultDict[int, List[int]]
        for c, pre in prerequisites:
            num_prereq[c] += 1
            opens_courses[pre].append(c)
        available = [i for i, count in enumerate(num_prereq) if not count]
        while available:
            curr = available.pop()
            for course in opens_courses[curr]:
                num_prereq[course] -= 1
                if not num_prereq[course]:
                    available.append(course)
        return not any(num_prereq)
