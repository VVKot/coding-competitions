"""
T: O(N!)
S: O(N)

In any case, we have to generate all possible palindromes, the question is
only how to do that efficiently. To avoid duplication, we just go over
characters and pick next character on each iteration. Decreasing and increasing
counts by two in the backtracking makes code cleaner and easier to comprehend.
"""

import collections
from typing import Counter, List


class Solution:

    def generatePalindromes(self, s: str) -> List[str]:
        char_count = collections.Counter(s)
        if not self.can_make_palindrome(char_count):
            return []
        palindromes = []
        middle_char = self.get_middle_char(char_count)

        def helper(current, counts):
            for char, count in counts.items():
                if count > 1:
                    counts[char] -= 2
                    current.appendleft(char)
                    current.append(char)
                    helper(current, counts)
                    counts[char] += 2
                    current.popleft()
                    current.pop()
            if len(current) == len(s):
                palindromes.append(''.join(current))

        initial_string = [middle_char] if middle_char else []
        helper(collections.deque(initial_string), char_count)
        return palindromes

    def can_make_palindrome(self, char_count: Counter[str]) -> bool:
        odd_counts = sum(count & 1 for count in char_count.values())
        return odd_counts <= 1

    def get_middle_char(self, char_count: Counter[str]) -> str:
        for char, count in char_count.items():
            if count & 1:
                return char
        return ""
