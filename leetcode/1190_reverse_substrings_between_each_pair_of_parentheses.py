from typing import List


class Solution:

    def reverseParentheses(self, s: str) -> str:
        curr = []  # type: List[str]
        stack = []
        for ch in s:
            if ch == '(':
                stack.append(curr)
                curr = []
            elif ch == ')':
                curr = stack.pop() + list(reversed(curr))
            else:
                curr.append(ch)
        return ''.join(curr)
