"""
T: O(N)
S: O(N)

Firstly, get the depth of the current element by counting tabs.
Secondly, we record the path length to the dictionary using depth as a key.
After that, we only have to extend the current path and compare it to the
longest path we have seen so far if the current element is a file.
"""


class Solution:

    TAB, DOT = '\t', '.'

    def lengthLongestPath(self, fs_path: str) -> int:
        longest = 0
        path_lens = {-1: 0}
        for path in fs_path.splitlines():
            depth = path.count(self.TAB)
            path_lens[depth] = path_lens[depth - 1] + len(path) - depth
            if self.DOT in path:
                longest = max(longest, path_lens[depth] + depth)
        return longest
