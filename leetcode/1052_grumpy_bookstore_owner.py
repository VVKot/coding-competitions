from typing import List


class Solution:

    def maxSatisfied(self,
                     customers: List[int],
                     grumpy: List[int],
                     X: int) -> int:
        N = len(customers)
        satisfied_count = sum(customers[i] for i in range(N)
                              if not grumpy[i])
        trick_len = min(N, X)
        tricked_count = sum(customers[i] for i in range(trick_len)
                            if grumpy[i])
        result = satisfied_count + tricked_count
        i = 0
        while i + X < N:
            if grumpy[i]:
                tricked_count -= customers[i]
            if grumpy[i + X]:
                tricked_count += customers[i + X]
            result = max(result, satisfied_count + tricked_count)
            i += 1
        return result
