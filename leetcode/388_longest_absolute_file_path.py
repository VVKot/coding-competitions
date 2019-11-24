"""
T: O(N)
S: O(N)

Firstly, we find current filename and level at which this file is located.
Secondly, we prune the current path if we jumped to a level closer to the root.
After that, we only have to extend current path and compare it to the longest
path we have seen so far if current element is a file.
"""


from typing import List, Tuple


class Solution:

    CARRIAGE_RETURN, TAB, DOT, SLASH = '\n', '\t', '.', '/'

    def lengthLongestPath(self, fs_path: str) -> int:
        longest_path_len = 0
        curr_path = []  # type: List[str]
        for path_part in self.get_path_parts(fs_path):
            file_name, file_level = self.get_file_info(path_part)
            if file_level < len(curr_path):
                curr_path = curr_path[:file_level]
            curr_path.append(file_name)
            if self.is_file(file_name):
                longest_path_len = max(longest_path_len,
                                       self.get_path_len(curr_path))
        return longest_path_len

    def get_path_parts(self, fs_path: str) -> List[str]:
        return fs_path.split(self.CARRIAGE_RETURN)

    def get_file_info(self, path_part: str) -> Tuple[str, int]:
        curr_row = path_part.split(self.TAB)
        curr_level = len(curr_row) - 1
        file_name = curr_row[0] if curr_level == 0 else curr_row[-1]
        return file_name, curr_level

    def is_file(self, file_name: str) -> bool:
        return self.DOT in file_name

    def get_path_len(self, curr_path: List[str]) -> int:
        return len(self.SLASH.join(curr_path))
