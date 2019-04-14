class ListNode():

    def __init__(self, x):
        self.val = x
        self.next = None


class MyLinkedList():

    def __init__(self):
        self.head = None
        self.size = 0

    def get(self, index):
        if not self.head or not 0 <= index < self.size:
            return -1
        curr = self.head
        for _ in range(index):
            curr = curr.next
        return curr.val

    def addAtHead(self, val):
        node = ListNode(val)
        node.next = self.head
        self.head = node
        self.size += 1

    def addAtTail(self, val):
        curr = self.head
        if curr is None:
            self.head = ListNode(val)
        else:
            while curr.next:
                curr = curr.next
            curr.next = ListNode(val)
        self.size += 1

    def addAtIndex(self, index, val):
        if index > self.size:
            return
        if index <= 0:
            self.addAtHead(val)
        else:
            curr = self.head
            for _ in range(index - 1):
                curr = curr.next
            node = ListNode(val)
            node.next = curr.next
            curr.next = node

            self.size += 1

    def deleteAtIndex(self, index):
        if not 0 <= index < self.size:
            return
        curr = self.head
        if not index:
            self.head = curr.next
        else:
            for _ in range(index - 1):
                curr = curr.next
            curr.next = curr.next.next
        self.size -= 1
