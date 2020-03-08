class Solution:

    def tribonacci(self, n: int) -> int:
        n1, n2, n3 = 0, 1, 1
        if n == 0:
            return n1
        if n < 3:
            return n3
        for _ in range(n-2):
            n3, n2, n1 = n3+n2+n1, n3, n2
        return n3
