class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 3:
            return 0
        primes = [2]
        for i in range(3, n, 2):
            is_prime = True
            for prime in primes:
                if prime > (math.sqrt(i)):
                    break
                if i % prime == 0:
                    is_prime = False
                    break
            if is_prime: primes.append(i)
        return len(primes)
