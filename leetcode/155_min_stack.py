class MinStack:

    def __init__(self):
        self.stack = []
        self.min_num = float('inf')

    def push(self, x: int) -> None:
        self.stack.append(x)
        self.min_num = min(self.min_num, x)

    def pop(self) -> None:
        removed = self.stack.pop()
        if removed == self.min_num:
            self.min_num = min(self.stack) if self.stack else float('inf')

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_num
