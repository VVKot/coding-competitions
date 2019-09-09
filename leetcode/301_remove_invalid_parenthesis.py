from typing import List


class Solution:

    def removeInvalidParentheses(self, s: str) -> List[str]:
        invalid_right = curr_left = 0
        for ch in s:
            if ch == '(':
                curr_left += 1
            elif ch == ')':
                if curr_left > 0:
                    curr_left -= 1
                else:
                    invalid_right += 1
        invalid_left = curr_left
        results = set()

        def helper(curr, position, left, right):
            if not left and not right:
                result = curr + s[position:]
                if self.is_valid(result):
                    results.add(result)
                return
            if position >= len(s):
                return
            if left and s[position] == '(':
                helper(curr, position+1, left-1, right)
            if right and s[position] == ')':
                helper(curr, position+1, left, right-1)
            helper(curr+s[position], position+1, left, right)
        helper('', 0, invalid_left, invalid_right)
        return list(results)

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
