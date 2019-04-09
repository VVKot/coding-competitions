class Solution:
    def diStringMatch(self, S):
        left, right, result = 0, len(S), []
        for ch in S:
            if ch == "I":
                result.append(left)
                left += 1
            else:
                result.append(right)
                right -= 1
        return result + [left]
