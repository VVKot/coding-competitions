from collections import OrderedDict


class LRUCache:
    def __init__(self, Capacity):
        self.capacity = Capacity
        self.cache = OrderedDict()

    def get(self, key):
        if key not in self.cache:
            return -1
        value = self.cache[key]
        self.cache.move_to_end(key)
        return value

    def put(self, key, value):
        if key in self.cache:
            del self.cache[key]
        self.cache[key] = value
        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)
