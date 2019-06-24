import random
from typing import List, Dict


class Solution:

    def __init__(self, N: int, blacklist: List[int]):
        blacklist = sorted(blacklist)
        black_set = set(blacklist)
        self.cap = N - len(black_set)
        self.subs = {}  # type: Dict[int, int]
        i = 0
        for num in range(self.cap, N):
            if num not in black_set:
                self.subs[blacklist[i]] = num
                i += 1

    def pick(self) -> int:
        num = random.randrange(0, self.cap)
        return self.subs[num] if num in self.subs else num
