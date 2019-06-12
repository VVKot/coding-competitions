import math
import random
from typing import List


class Solution:

    def __init__(self, radius: float, x_center: float, y_center: float):
        self.radius = radius
        self.x_center = x_center
        self.y_center = y_center

    def randPoint(self) -> List[float]:
        dist = math.sqrt(random.random()) * self.radius
        degree = random.random() * 2 * math.pi
        x = self.x_center + dist * math.cos(degree)
        y = self.y_center + dist * math.sin(degree)
        return [x, y]
