class Solution:

    def integerBreak(self, n: int) -> int:
        if n == 2:
            return 1
        elif n == 3:
            return 2
        elif not n % 3:
            return 3 ** (n//3)
        elif n % 3 == 1:
            return 2 * 2 * 3 ** ((n-4)//3)
        else:
            return 2 * 3 ** ((n-2)//3)
