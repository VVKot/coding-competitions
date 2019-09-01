import math


class Solution:

    MAX_NUM = 10**9 + 7

    def numPrimeArrangements(self, n: int) -> int:
        prime_count = 0
        for i in range(2, n+1):
            if self.is_prime(i):
                prime_count += 1
        return math.factorial(prime_count) * \
            math.factorial(n-prime_count) % self.MAX_NUM

    def is_prime(self, val: int) -> bool:
        for i in range(2, val):
            if val % i == 0:
                return False
        return True
