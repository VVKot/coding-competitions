from typing import List


class Solution:

    NUM_OF_COLORS = 3

    def shortestDistanceColor(self,
                              colors: List[int],
                              queries: List[List[int]]) -> List[int]:
        lefts = self.get_left_positions(colors)
        rights = self.get_right_positions(colors)
        distances = []
        for i, color in queries:
            color -= 1
            distance = i - lefts[color][i]
            distance = min(distance, rights[color][i] - i)
            distances.append(-1 if distance == float('inf') else distance)
        return distances

    def get_left_positions(self, colors: List[int]) -> List[List[float]]:
        N = len(colors)
        left = [[float('-inf') for _ in range(N)]
                for _ in range(self.NUM_OF_COLORS)]
        last = [float('-inf'), float('-inf'), float('-inf')]
        for i in range(N):
            color = colors[i]-1
            last[color] = i
            for j in range(self.NUM_OF_COLORS):
                left[j][i] = last[j]
        return left

    def get_right_positions(self, colors: List[int]) -> List[List[float]]:
        N = len(colors)
        right = [[float('inf') for _ in range(N)]
                 for _ in range(self.NUM_OF_COLORS)]
        last = [float('inf'), float('inf'), float('inf')]
        for i in reversed(range(N)):
            color = colors[i]-1
            last[color] = i
            for j in range(self.NUM_OF_COLORS):
                right[j][i] = last[j]
        return right
