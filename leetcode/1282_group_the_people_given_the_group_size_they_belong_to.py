"""
T: O(N)
S: O(N)

Collect groups of the same size.
When the group is full - push it to the result.
"""

import collections
from typing import Dict, List


class Solution:

    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        size_indices = \
            collections.defaultdict(list)  # type: Dict[int, List[int]]
        groups = []
        for i, size in enumerate(groupSizes):
            size_indices[size].append(i)
            if len(size_indices[size]) == size:
                groups.append(size_indices[size][:])
                size_indices[size] = []
        return groups
