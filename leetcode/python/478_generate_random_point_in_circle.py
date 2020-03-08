import random
from typing import List


class Solution:

    def __init__(self, radius: float, x_center: float, y_center: float):
        self.radius = radius
        self.x_center = x_center
        self.y_center = y_center
        self.x_min, self.x_max = x_center - radius, x_center + radius
        self.y_min, self.y_max = y_center - radius, y_center + radius

    def randPoint(self) -> List[float]:
        while True:
            x = random.uniform(self.x_min, self.x_max)
            y = random.uniform(self.y_min, self.y_max)
            dist = (x - self.x_center) ** 2 + (y - self.y_center) ** 2
            if dist <= self.radius ** 2:
                return [x, y]
