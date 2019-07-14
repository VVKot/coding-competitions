from typing import List


class Solution:

    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        amount = 1
        distribution = [0] * num_people
        while candies:
            for i in range(num_people):
                candies_to_give = min(amount, candies)
                candies -= candies_to_give
                distribution[i] += candies_to_give
                amount += 1
        return distribution
