"""
T: O(N)
S: O(N)

Process every character, check if it is the same as the previous one. If so -
don't put it into the stack and pop the last character in the stack. This way,
our algorithm will work even when we have to do multiple removals in one go,
i.e. for abba, because bb will never be added to the stack.
"""

from typing import List


class Solution:

    def removeDuplicates(self, S: str) -> str:
        stack = []  # type: List[str]
        for char in S:
            if not stack or stack[-1] != char:
                stack.append(char)
            else:
                stack.pop()
        return "".join(stack)
