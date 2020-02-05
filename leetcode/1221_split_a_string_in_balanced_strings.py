"""
T: O(N)
S: O(1)

We use the fact that initial string is balanced. If the previous found
interval is balanced, then the next interval is either balanced or empty.
It it wasn't so - the whole string would not be balanced, which contradicts
the inital propmt
"""

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
