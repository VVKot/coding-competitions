"""
T: O(N)
S: O(1)

The solution without language built-ins that does not allocate additional
memory. Check if the previous character is space and current is not - that is
the beginning of the new segment.
"""


class Solution:

    def countSegments(self, s: str) -> int:
        segment_count = 0
        for i, char in enumerate(s):
            if i == 0 or s[i - 1].isspace():
                if not char.isspace():
                    segment_count += 1
        return segment_count
