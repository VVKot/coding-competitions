from typing import List


class Solution:

    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        amount = 0
        distribution = [0] * num_people
        while candies:
            to_give = min(amount+1, candies)
            distribution[amount % num_people] += to_give
            amount += 1
            candies -= to_give
        return distribution
