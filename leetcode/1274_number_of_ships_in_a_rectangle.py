"""
T: O(logN)
S: O(logN)

Recursively divide the grid into four squares and visit them if they have
ships.
"""


class Sea(object):

    def hasShips(self, topRight: 'Point', bottomLeft: 'Point') -> bool:
        return True


class Point(object):

    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y


class Solution(object):

    def countShips(self, sea: 'Sea', topRight: 'Point',
                   bottomLeft: 'Point') -> int:
        ship_count = 0
        if topRight.x >= bottomLeft.x and topRight.y >= bottomLeft.y \
                and sea.hasShips(topRight, bottomLeft):
            if topRight.x == bottomLeft.x and topRight.y == bottomLeft.y:
                return 1
            mid_x, mid_y = (topRight.x + bottomLeft.x) // 2, \
                (topRight.y + bottomLeft.y) // 2
            ship_count += self.countShips(sea, Point(mid_x, mid_y), bottomLeft)
            ship_count += self.countShips(sea, Point(mid_x, topRight.y),
                                          Point(bottomLeft.x, mid_y + 1))
            ship_count += self.countShips(sea, Point(topRight.x, mid_y),
                                          Point(mid_x + 1, bottomLeft.y))
            ship_count += self.countShips(sea, topRight,
                                          Point(mid_x + 1, mid_y + 1))
        return ship_count
