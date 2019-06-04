import random
from typing import List


class ListNode:

    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:

    def __init__(self, head: ListNode):
        self.head = head

    def getRandom(self) -> int:
        count = 0
        random_val = -1
        curr = self.head
        while curr:
            if random.randint(0, count) == 0:
                random_val = curr.val
            count += 1
            curr = curr.next
        return random_val
