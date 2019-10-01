class Solution:

    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        str_representation = str(x)
        return str_representation == str_representation[::-1]
