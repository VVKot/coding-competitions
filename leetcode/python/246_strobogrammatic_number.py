class Solution:

    def isStrobogrammatic(self, num: str) -> bool:
        strobogrammatic_pairs = {('0', '0'), ('1', '1'), ('8', '8'), ('6', '9'),
                                 ('9', '6')}
        left, right = 0, len(num) - 1
        while left <= right:
            current_pair = (num[left], num[right])
            if current_pair not in strobogrammatic_pairs:
                return False
            left += 1
            right -= 1
        return True
