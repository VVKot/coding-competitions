"""
T: O(logN)
S: O(1)

Do as the description says, compute sum and product.
After that compute the result.
"""


class Solution:

    def subtractProductAndSum(self, n: int) -> int:
        digit_sum, digit_product = 0, 1
        while n > 0:
            n, mod = divmod(n, 10)
            digit_sum += mod
            digit_product *= mod
        return digit_product - digit_sum
