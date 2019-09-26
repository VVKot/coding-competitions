class Solution:

    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        if x == 0:
            return 0
        power = 1
        if n < 0:
            x = 1/x
            n = -n
        power_values = {1: x}
        while power < n:
            power *= 2
            x *= x
            power_values[power] = x
        if power == n:
            return x
        power //= 2
        remainder = n - power
        x = power_values[power]
        while remainder:
            power //= 2
            if power <= remainder:
                remainder -= power
                x *= power_values[power]
        return x
