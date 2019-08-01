from typing import List


class Solution:

    def camelMatch(self, queries: List[str], pattern: str) -> List[bool]:
        return [self.is_camel_match(query, pattern) for query in queries]

    def is_camel_match(self, query: str, pattern: str) -> bool:
        Q = len(query)
        P = len(pattern)
        i = j = 0
        while i < Q and j < P:
            if query[i] == pattern[j]:
                j += 1
            elif query[i].isupper():
                return False
            i += 1
        return j >= P and (i >= Q or query[i:].islower())
