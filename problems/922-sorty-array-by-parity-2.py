class Solution:
    def sortArrayByParityII(self, A):
        odd_oop = []
        even_oop = []
        for i, num in enumerate(A):
            if num % 2 == 1 and i % 2 == 0:
                if even_oop:
                    even_idx = even_oop.pop()
                    A[i], A[even_idx] = A[even_idx], A[i]
                else:
                    odd_oop.append(i)

            if num % 2 == 0 and i % 2 == 1:
                if odd_oop:
                    odd_idx = odd_oop.pop()
                    A[i], A[odd_idx] = A[odd_idx], A[i]
                else:
                    even_oop.append(i)
        return A
