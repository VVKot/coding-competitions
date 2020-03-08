import random


class RandomizedCollection:

    def __init__(self):
        self.L = {}
        self.N = []

    def insert(self, val: int) -> bool:
        result = val not in self.L
        if result:
            self.L[val] = set()
        self.L[val].add(len(self.N))
        self.N.append(val)
        return result

    def remove(self, val: int) -> bool:
        if val not in self.L:
            return False
        loc = self.L[val].pop()
        tail_index = len(self.N) - 1
        if loc != tail_index:
            last = self.N[-1]
            self.N[-1], self.N[loc] = self.N[loc], self.N[-1]
            self.L[last].remove(tail_index)
            self.L[last].add(loc)
        self.N.pop()
        if not self.L[val]:
            del self.L[val]
        return True

    def getRandom(self) -> int:
        return random.choice(self.N)
