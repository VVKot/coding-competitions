class Solution:

    def balancedStringSplit(self, s: str) -> int:
        split_count = current_balance = 0
        for ch in s:
            if ch == 'R':
                current_balance += 1
            else:
                current_balance -= 1
            if current_balance == 0:
                split_count += 1
        return split_count
