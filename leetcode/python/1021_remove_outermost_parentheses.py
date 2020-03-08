class Solution:

    def removeOuterParentheses(self, S: str) -> str:
        result = ""
        left, right, start = 0, 0, 0
        for i, ch in enumerate(S):
            if ch == '(':
                left += 1
            else:
                right += 1
            if left and right and left == right:
                result += S[start+1:i]
                start = i + 1
                left = 0
                right = 0
        return result
