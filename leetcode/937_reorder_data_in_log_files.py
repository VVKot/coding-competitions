"""
T: O(NlogN)
S: O(N)

Compress requirements into the one lambda.
All that we have to check is the first letter of the first word.
"""


from typing import List, Tuple


class Solution:

    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        return sorted(logs, key=self.sort_lambda)

    def sort_lambda(self, log: str) -> Tuple[int, str, str]:
        identifier, words = log.split(' ', 1)
        return (0, words, identifier) if words[0].isalpha() else (1, '', '')
