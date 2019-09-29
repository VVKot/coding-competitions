class Solution:

    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        N = len(s)
        max_substring = 0
        total_cost = 0
        left = 0
        for right in range(N):
            total_cost += self._get_cost(s[right], t[right])
            while total_cost > maxCost and left < N:
                total_cost -= self._get_cost(s[left], t[left])
                left += 1
            max_substring = max(max_substring, right-left+1)
        return max_substring

    def _get_cost(self, s: str, t: str) -> int:
        return abs(ord(s) - ord(t))
