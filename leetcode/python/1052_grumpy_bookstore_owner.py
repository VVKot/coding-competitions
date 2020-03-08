from typing import List


class Solution:

    def maxSatisfied(self,
                     customers: List[int],
                     grumpy: List[int],
                     X: int) -> int:
        already_satisfied = max_tricked = current_tricked = 0
        for i, count in enumerate(customers):
            if grumpy[i]:
                current_tricked += count
            else:
                already_satisfied += count
            if i >= X:
                current_tricked -= grumpy[i - X] * customers[i - X]
            max_tricked = max(max_tricked, current_tricked)
        return already_satisfied + max_tricked
