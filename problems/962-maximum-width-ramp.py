class Solution:
    def maxWidthRamp(self, A):
        result = 0
        if not A:
            return result
        stack = []
        for i, num in enumerate(A):
            if not stack or A[stack[-1]] > num:
                stack.append(i)
        for j in reversed(range(len(A))):
            while stack and A[stack[-1]] <= A[j]:
                result = max(result, j - stack.pop())
        return result
