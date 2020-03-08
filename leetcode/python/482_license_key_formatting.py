"""
T: O(N)
S: O(N)

The solution is easy if we reverse the process.
Start building groups from the back.
Insert a dash if you see a new alphanumeric character,
and the previous group is full.
"""


class Solution:

    DASH = '-'

    def licenseKeyFormatting(self, S: str, K: int) -> str:
        formatted_key = []
        curr_group_count = 0
        for ch in reversed(S.upper()):
            if ch != self.DASH:
                if curr_group_count == K:
                    curr_group_count = 0
                    formatted_key.append(self.DASH)
                formatted_key.append(ch)
                curr_group_count += 1
        return ''.join(reversed(formatted_key))
