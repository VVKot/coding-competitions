class Solution:
    def is_odd(self, num):
        return num % 2

    def is_even(self, num):
        return not self.is_odd(num)

    def sortArrayByParity(self, A):
        write = 0
        read = 0
        while read != len(A):
            read_el = A[read]
            if self.is_even(read_el):
                write_el = A[write]
                if self.is_odd(write_el):
                    A[read], A[write] = A[write], A[read]
                write += 1
            read += 1
        return A
