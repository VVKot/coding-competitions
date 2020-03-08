from typing import List


class Solution:

    def lexicalOrder(self, n: int) -> List[int]:
        result = []

        def helper(curr):
            if curr > n:
                return
            result.append(curr)
            helper(curr * 10)
            if (curr + 1) % 10:
                helper(curr + 1)
        helper(1)
        return result
