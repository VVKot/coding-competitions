import collections
import bisect


class TimeMap:

    def __init__(self):
        self.keys = collections.defaultdict(list)
        self.vals = collections.defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.keys[key].append(timestamp)
        self.vals[key].append(value)

    def get(self, key: str, timestamp: int) -> str:
        index = bisect.bisect(self.keys[key], timestamp)
        return self.vals[key][index - 1] if index else ''
