
class Solution:

    def isPowerOfThree(self, n: int) -> bool:
        if n < 1:
            return False
        while not n % 3:
            n //= 3
        return n == 1
