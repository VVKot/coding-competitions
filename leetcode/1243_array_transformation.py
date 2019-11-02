from typing import List


class Solution:

    def transformArray(self, arr: List[int]) -> List[int]:
        def make_new(old):
            N = len(old)
            new = old[:]
            for i in range(1, N-1):
                if old[i-1] < old[i] > old[i+1]:
                    new[i] -= 1
                if old[i-1] > old[i] < old[i+1]:
                    new[i] += 1
            return new

        while True:
            new_arr = make_new(arr)
            if new_arr == arr:
                return new_arr
            arr = new_arr
