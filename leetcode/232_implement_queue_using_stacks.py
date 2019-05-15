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
        while len(self.master):
            top = self.master.pop()
            self.slave.append(top)
        self.master.append(x)
        while len(self.slave):
            top = self.slave.pop()
            self.master.append(top)

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        return self.master.pop()

    def peek(self) -> int:
        """
        Get the front element.
        """
        return self.master[-1]

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return not len(self.master)
