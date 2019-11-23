"""
T: O(N)
S: O(N)

We should considered all of three case. If a domino is still,
it might be required to be flipped on the path to the right.
When going to the right, just flip every domino to the right and record
the distance from the first falling domino. On the path to the left, compare
those distance to decide if domino should be falling or still if it has
falling neighbors from both sides.
"""


class Solution:

    LEFT, RIGHT, STILL = 'L', 'R', '.'

    def pushDominoes(self, dominoes: str) -> str:
        N = len(dominoes)
        pushed_dominoes = list(dominoes)
        travel_distance = [0.0 for _ in range(N)]
        for i, direction in enumerate(pushed_dominoes):
            if direction == self.RIGHT:
                j = i + 1
                curr_distance = 1
                while j < N and pushed_dominoes[j] == self.STILL:
                    travel_distance[j] = curr_distance
                    pushed_dominoes[j] = self.RIGHT
                    curr_distance += 1
                    j += 1
            elif direction == self.LEFT:
                j = i - 1
                curr_distance = 1
                while j >= 0:
                    if curr_distance < travel_distance[j]:
                        pushed_dominoes[j] = self.LEFT
                    else:
                        if curr_distance == travel_distance[j]:
                            pushed_dominoes[j] = self.STILL
                        break
                    curr_distance += 1
                    j -= 1
            else:
                travel_distance[i] = float('inf')
        return ''.join(pushed_dominoes)
