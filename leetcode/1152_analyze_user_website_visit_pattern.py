import collections
import itertools
from typing import Counter, DefaultDict, List, Tuple


class Solution:
    def mostVisitedPattern(self,
                           username: List[str],
                           timestamp: List[int],
                           website: List[str]) -> List[str]:
        user_visits = \
            collections.defaultdict(list)  # type: DefaultDict[str, List[str]]
        for t, u, w in sorted(zip(timestamp, username, website)):
            user_visits[u].append(w)
        patterns = collections.Counter()  # type: Counter[Tuple[str, ...]]
        for visited in user_visits.values():
            patterns += collections.Counter(
                set(itertools.combinations(visited, 3)))
        return list(min(patterns, key=lambda x: (-patterns[x], x)))
