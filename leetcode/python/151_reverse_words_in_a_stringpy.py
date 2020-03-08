"""
T: O(N)
S: O(N)

Just do as the description says. Python's split correctly handles leading
and trailing whitespace and properly splits on multiple whitespace chars.
"""


class Solution:

    def reverseWords(self, s: str) -> str:
        return ' '.join(reversed(s.split()))