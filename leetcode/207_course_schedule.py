from collections import deque


class Solution:

    def canFinish(self, numCourses, prerequisites):
        courses = [[] for _ in range(numCourses)]
        in_degrees = [0] * numCourses
        for after, pre in prerequisites:
            courses[pre].append(after)
            in_degrees[after] += 1
        to_study = deque()
        for i, num in enumerate(in_degrees):
            if not num:
                to_study.append(i)
        studied = 0
        while to_study:
            curr = to_study.popleft()
            studied += 1
            opened = courses[curr]
            for c in opened:
                in_degrees[c] -= 1
            if not in_degrees[c]:
                to_study.append(c)
        return studied == numCourses
