class Solution:

    def isLongPressedName(self, name: str, typed: str) -> bool:
        i = 0
        N = len(name)
        T = len(typed)
        for j in range(T):
            if i < N and name[i] == typed[j]:
                i += 1
            elif not j or typed[j] != typed[j-1]:
                return False
        return i == N
