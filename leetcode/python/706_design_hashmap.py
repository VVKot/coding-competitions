class ListNode:

    def __init__(self, key: int, val: int):
        self.pair = (key, val)
        self.next = None


class MyHashMap:

    def __init__(self):
        self.size = 1000
        self.store = [None] * self.size

    def _get_hash(self, key):
        return key % self.size

    def put(self, key: int, value: int) -> None:
        hash = self._get_hash(key)
        if self.store[hash] is None:
            self.store[hash] = ListNode(key, value)
        else:
            curr = self.store[hash]
            while True:
                if curr.pair[0] == key:
                    curr.pair = (key, value)
                    return
                if curr.next is None:
                    break
                curr = curr.next
            curr.next = ListNode(key, value)

    def get(self, key: int) -> int:
        hash = self._get_hash(key)
        curr = self.store[hash]
        while curr:
            if curr.pair[0] == key:
                return curr.pair[1]
            else:
                curr = curr.next
        return -1

    def remove(self, key: int) -> None:
        hash = self._get_hash(key)
        curr = prev = self.store[hash]
        if not curr:
            return
        if curr.pair[0] == key:
            self.store[hash] = curr.next
        else:
            curr = curr.next
            while curr:
                if curr.pair[0] == key:
                    prev.next = curr.next
                    break
                else:
                    curr, prev = curr.next, prev.next
