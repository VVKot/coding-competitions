class Solution:

    def scoreOfParentheses(self, S: str) -> int:
        depth, result = 0, 0
        for i, ch in enumerate(S):
            if ch == '(':
                depth += 1
            else:
                if S[i-1] == '(':
                    result += 1 << (depth - 1)
                depth -= 1
        return result
