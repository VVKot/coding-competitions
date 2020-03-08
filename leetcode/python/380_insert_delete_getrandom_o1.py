import random


class RandomizedSet:

    def __init__(self):
        self.values = []
        self.indices = {}

    def insert(self, val: int) -> bool:
        if val in self.indices:
            return False
        self.indices[val] = len(self.values)
        self.values.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.indices:
            return False
        val_index = self.indices[val]
        last_val = self.values[-1]
        self.indices[last_val] = val_index
        self.values[val_index], self.values[-1] = \
            self.values[-1], self.values[val_index]
        del self.indices[val]
        self.values.pop()
        return True

    def getRandom(self) -> int:
        return random.choice(self.values)
