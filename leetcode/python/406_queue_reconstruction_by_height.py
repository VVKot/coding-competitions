from typing import List


class Solution:

    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        result = []  # type: List[List[int]]
        people = sorted(people, key=lambda x: (-x[0], x[1]))
        for h, k in people:
            result.insert(k, [h, k])
        return result
