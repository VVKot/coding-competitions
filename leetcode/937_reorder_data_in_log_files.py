"""
T: O(NlogN)
S: O(N)

First, split logs into separate groups.
After that, letter logs are sorted by words,
and by the identifier in the case of a tie.
"""


from typing import List


class Solution:

    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letter_logs = []
        digit_logs = []
        for log in logs:
            if log.split()[1].isnumeric():
                digit_logs.append(log)
            else:
                letter_logs.append(log)
        letter_logs.sort(key=self.sort_lambda)
        return letter_logs + digit_logs

    def sort_lambda(self, log: str) -> List[str]:
        words = log.split()
        words.append(words.pop(0))
        return words
