class Solution:
    def minAddToMakeValid(self, S: str) -> int:
        left_count, result = 0, 0
        for ch in S:
            if ch == '(':
                left_count += 1
            elif not left_count:
                result += 1
            else:
                left_count -= 1
        return result + left_count
