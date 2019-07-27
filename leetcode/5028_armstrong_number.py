class Solution:

    def isArmstrong(self, N: int) -> bool:
        K = len(str(N))
        total = 0
        for i in (int(j) for j in str(N)):
            total += i ** K
        return total == N
