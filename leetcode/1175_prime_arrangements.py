import math


class Solution:

    MAX_NUM = 10**9 + 7

    def numPrimeArrangements(self, n: int) -> int:
        prime_count = self.get_prime_count(n)
        return math.factorial(prime_count) * \
            math.factorial(n-prime_count) % self.MAX_NUM

    def get_prime_count(self, val: int) -> int:
        is_prime = [True] * (val+1)
        is_prime[0] = is_prime[1] = False
        max_divisor = math.ceil(math.sqrt(val)) + 1
        for i in range(2, max_divisor):
            if is_prime[i]:
                j = i*i
                while j <= val:
                    is_prime[j] = False
                    j += i
        return sum(is_prime)
