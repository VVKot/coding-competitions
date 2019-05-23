class Solution:

    def backspaceCompare(self, S: str, T: str) -> bool:
        S = self.get_res(S)
        T = self.get_res(T)
        return S == T

    def get_res(self, seq):
        stack = []
        for ch in seq:
            if ch == '#':
                if stack:
                    stack.pop()
            else:
                stack.append(ch)
        return ''.join(stack)
