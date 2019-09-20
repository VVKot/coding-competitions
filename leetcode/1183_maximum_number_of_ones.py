class Solution:

    def maximumNumberOfOnes(self,
                            width: int,
                            height: int,
                            s: int,
                            maxOnes: int) -> int:
        allowed_square_mapping = [0] * (s**2)
        for y in range(height):
            for x in range(width):
                position = (y % s) * s + x % s
                allowed_square_mapping[position] += 1
        allowed_square_mapping.sort()
        result = 0
        for _ in range(maxOnes):
            result += allowed_square_mapping.pop()
        return result
