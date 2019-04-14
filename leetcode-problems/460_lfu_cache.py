from collections import defaultdict, OrderedDict


class LFUCache(object):
    def __init__(self, capacity):
        self.remaining_capacity = capacity
        self.node_freq = defaultdict(OrderedDict)
        self.min_freq = 1
        self.node_keys = {}

    def _update(self, key, newValue=None):
        value, freq = self.node_keys[key]
        if newValue is not None:
            value = newValue
        self.node_freq[freq].pop(key)
        if not len(self.node_freq[self.min_freq]):
            self.min_freq += 1
        self.node_freq[freq+1][key] = value
        self.node_keys[key] = (value, freq+1)

    def get(self, key):
        if key not in self.node_keys:
            return -1
        self._update(key)
        return self.node_keys[key][0]

    def put(self, key, value):
        if key in self.node_keys:
            self._update(key, value)
        else:
            self.node_keys[key] = (value,1)
            self.node_freq[1][key] = value
            if not self.remaining_capacity:
                removed = self.node_freq[self.min_freq].popitem(last=False)
                self.node_keys.pop(removed[0])
            else:
                self.remaining_capacity -= 1
            self.min_freq = 1