from typing import Dict, List


class Solution:

    def knightDialer(self, N: int) -> int:
        num_dials = {i: 1 for i in range(10)}
        near = {0: [4, 6], 1: [6, 8], 2: [7, 9], 3: [4, 8],
                4: [0, 3, 9], 5: [], 6: [0, 1, 7], 7: [2, 6],
                8: [1, 3], 9: [2, 4]}  # type: Dict[int, List[int]]
        for _ in range(N-1):
            dials = dict(num_dials)
            for i in range(10):
                near_sum = sum(num_dials[j] for j in near[i])
                dials[i] = near_sum
            num_dials = dials
        return sum(num_dials.values()) % (10**9 + 7)
