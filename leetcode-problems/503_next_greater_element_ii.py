class Solution:
    def nextGreaterElements(self, A):
        stack, res = [], [-1] * len(A)
        for i in range(len(A)):
            while stack and (A[stack[-1]] < A[i]):
                res[stack.pop()] = A[i]
            stack.append(i)
        for i in range(len(A)):
            while stack and (A[stack[-1]] < A[i]):
                res[stack.pop()] = A[i]
            stack.append(i)
        return res
