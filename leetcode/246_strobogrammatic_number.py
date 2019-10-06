class Solution:

    def isStrobogrammatic(self, num: str) -> bool:
        pairs = {
            ('0', '0'),
            ('1', '1'),
            ('8', '8'),
            ('6', '9'),
            ('9', '6')
        }
        digits = list(str(num))
        left, right = 0, len(digits)-1
        while left <= right:
            current_pair = (digits[left], digits[right])
            if current_pair not in pairs:
                return False
            left += 1
            right -= 1
        return True
