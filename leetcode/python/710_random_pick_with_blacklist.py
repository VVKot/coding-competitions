import random
from typing import List, Dict


class Solution:

    def __init__(self, N: int, blacklist: List[int]):
        black_set = set(blacklist)
        self.cap = N - len(black_set)
        self.subs = {}  # type: Dict[int, int]
        i = self.cap
        for num in black_set:
            if num < self.cap:
                while i in black_set:
                    i += 1
                self.subs[num] = i
                i += 1

    def pick(self) -> int:
        num = random.randrange(0, self.cap)
        return self.subs[num] if num in self.subs else num
