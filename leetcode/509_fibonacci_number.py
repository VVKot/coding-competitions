class Solution:
    def fib(self, N: int) -> int:
        first, second = 0, 1
        for _ in range(N):
            first, second = second, first + second
        return first
