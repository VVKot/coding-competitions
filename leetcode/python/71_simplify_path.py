"""
T: O(N)
S: O(N)

Firstly, split the path into separate directory names.
After that, maintain a stack of directories on the current path.
If we see a couple of dots, we go one level up. Dot and empty dir name
is a no-op.
"""


import re
from typing import List


class Solution:

    CURR_DIR, PREV_DIR, EMPTY, SLASH = '.', '..', '', '/'

    def simplifyPath(self, path: str) -> str:
        dir_stack = []  # type: List[str]
        dir_list = re.split('/+', path)
        for curr_dir in dir_list:
            if curr_dir == self.PREV_DIR:
                if dir_stack:
                    dir_stack.pop()
            elif curr_dir != self.CURR_DIR and curr_dir != self.EMPTY:
                dir_stack.append(curr_dir)
        return self.SLASH + self.SLASH.join(dir_stack)
