from functools import lru_cache
from typing import List


class Solution:

    def dieSimulator(self, n: int, rollMax: List[int]) -> int:
        MOD = 10 ** 9 + 7
        DIE_SIDES = 6

        @lru_cache(None)
        def dp(rolls_to_generate, last_roll, last_roll_times):
            if rolls_to_generate == 0:
                return 1
            res = 0
            for i in range(DIE_SIDES):
                if i != last_roll:
                    res += dp(rolls_to_generate-1, i, 1)
                elif last_roll_times < rollMax[i]:
                    res += dp(rolls_to_generate-1, i, last_roll_times+1)
            return res

        return dp(n, -1, 0) % MOD
