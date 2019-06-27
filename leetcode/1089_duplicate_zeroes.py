from typing import List


class Solution:

    def duplicateZeros(self, arr: List[int]) -> None:
        N = len(arr)
        shift = arr.count(0)
        for i in reversed(range(N)):
            if i + shift < N:
                arr[i + shift] = arr[i]
            if not arr[i]:
                shift -= 1
                if i + shift < N:
                    arr[i + shift] = arr[i]