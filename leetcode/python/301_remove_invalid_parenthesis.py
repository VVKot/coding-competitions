from typing import List


class Solution:

    def removeInvalidParentheses(self, s: str) -> List[str]:
        level = {s}
        while True:
            valid = list(filter(self.is_valid, level))
            if valid:
                return valid
            level = {s[:i] + s[i+1:] for s in level for i in range(len(s))}

    def is_valid(self, s: str) -> bool:
        left = 0
        for ch in s:
            if ch == '(':
                left += 1
            elif ch == ')':
                if not left:
                    return False
                left -= 1
        return not left
