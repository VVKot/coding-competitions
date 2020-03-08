class Solution:

    def fib(self, N: int) -> int:
        curr, next = 0, 1
        for _ in range(N):
            curr, next = next, curr + next
        return curr
