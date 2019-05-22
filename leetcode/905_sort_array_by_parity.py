from typing import List


class Solution:

    def sortArrayByParity(self, A: List[int]) -> List[int]:
        A.sort(key=lambda x: x & 1)
        return A
