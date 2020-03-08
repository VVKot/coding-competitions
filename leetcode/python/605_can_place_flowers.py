class Solution:
    def canPlaceFlowers(self, flowerbed, n):
        empty = 0
        flowerbed.insert(0, 0)
        flowerbed.append(0)
        for f in flowerbed:
            if not f:
                empty += 1
            else:
                empty = 0
            if empty == 3:
                n -= 1
                empty = 1
            if not n:
                return True
        return False
