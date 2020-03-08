class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.master = []
        self.slave = []

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.slave.push()

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        if not self.master:
            self.move()
        return self.master.pop()

    def peek(self) -> int:
        """
        Get the front element.
        """
        if not self.master:
            self.move()
        return self.master[-1]

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return not len(self.master) and not len(self.slave)

    def move(self) -> None:
        while self.slave:
            self.master.push(self.slave.pop())