class Solution:

    three_to_nineteenth = 1162261467

    def isPowerOfThree(self, n: int) -> bool:
        return n > 0 and not self.three_to_nineteenth % n
