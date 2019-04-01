from collections import deque


class Solution:
    def sortedSquares(self, A):
        if not A:
            return []
        print(A)
        result = deque()
        left, right = 0, len(A) - 1
        while left <= right:
            at_left, at_right = abs(A[left]), abs(A[right])
            if at_left > at_right:
                result.appendleft(at_left * at_left)
                left += 1
            else:
                result.appendleft(at_right * at_right)
                right -= 1
        return list(result)
