import random
from typing import List


class ListNode:

    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:

    def __init__(self, head: ListNode):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null.
        """
        self.store = []  # type: List[int]
        while head:
            self.store.append(head.val)
            head = head.next

    def getRandom(self) -> int:
        """
        Returns a random node's value.
        """
        random_index = random.randint(0, len(self.store) - 1)
        return self.store[random_index]
