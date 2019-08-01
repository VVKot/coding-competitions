from typing import List


class Solution:

    def camelMatch(self, queries: List[str], pattern: str) -> List[bool]:
        return [self.is_camel_match(query, pattern) for query in queries]

    def is_camel_match(self, query: str, pattern: str) -> bool:
        P = len(pattern)
        j = 0
        for ch in query:
            if j < P and pattern[j] == ch:
                j += 1
            elif ch.isupper():
                return False
        return j == P
