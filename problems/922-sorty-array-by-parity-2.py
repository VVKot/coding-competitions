class Solution:
    def sortArrayByParityII(self, A):
        i = 0
        j = 1
        N = len(A)
        while i < N and j < N:
            if A[i] % 2 == 0:
                i += 2
            elif A[j] % 2 == 1:
                j += 2
            else:
                A[i], A[j] = A[j], A[i]
                i += 2
                j += 2
        return A