from functools import lru_cache


class Solution:

    HAPPY = 1

    def isHappy(self, n: int) -> bool:
        slow = fast = n
        while True:
            slow = self.get_next(slow)
            fast = self.get_next(self.get_next(fast))
            if slow == self.HAPPY or fast == self.HAPPY:
                return True
            if slow == fast:
                return False

    @lru_cache(None)
    def get_next(self, n: int) -> int:
        next_num = 0
        while n:
            n, last_digit = divmod(n, 10)
            next_num += last_digit ** 2
        return next_num
