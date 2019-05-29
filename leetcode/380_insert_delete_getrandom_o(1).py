from random import randint


class RandomizedSet:

    def __init__(self):
        self.nums = []
        self.locs = {}

    def insert(self, val: int) -> bool:
        if val in self.locs:
            return False
        self.locs[val] = len(self.nums)
        self.nums.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.locs:
            return False
        loc = self.locs[val]
        if loc != len(self.nums) - 1:
            last = self.nums[-1]
            self.nums[-1], self.nums[loc] = self.nums[loc], self.nums[-1]
            self.locs[last] = loc
        del self.locs[val]
        self.nums.pop()
        return True

    def getRandom(self) -> int:
        random_index = randint(0, len(self.nums) - 1)
        return self.nums[random_index]
