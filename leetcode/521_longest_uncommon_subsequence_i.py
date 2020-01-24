"""
T: O(max(A, B))
S: O(1)

If strings are equal return -1 since there is no subsequence that can be made.
Otherwise, return the length of the longest string since it can not be a
subsequence of a smaller or different same-length string.
"""


class Solution:

    def findLUSlength(self, a: str, b: str) -> int:
        if a == b:
            return -1
        return max(len(a), len(b))
