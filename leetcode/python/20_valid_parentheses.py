class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for ch in s:
            curr = stack[-1] if stack else ''
            if curr == ch:
                stack.pop()
                continue
            elif ch == '{':
                stack.append('}')
            elif ch == '(':
                stack.append(')')
            elif ch == '[':
                stack.append(']')
            else:
                return False
        return not len(stack)
