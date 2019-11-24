"""
T: O(N)
S: O(N)

First, we create a map from parent process to all its childs.
After that, we traverse it in DFS fashion and collection process ids.
"""


import collections
from typing import Dict, List


class Solution:

    def killProcess(self,
                    pid: List[int],
                    ppid: List[int],
                    kill: int) -> List[int]:
        parent_map = \
            collections.defaultdict(list)  # type: Dict[int, List[int]]
        for process, parent in zip(pid, ppid):
            parent_map[parent].append(process)
        pids_to_kill = [kill]
        killed_process = []
        while pids_to_kill:
            curr_pid = pids_to_kill.pop()
            killed_process.append(curr_pid)
            pids_to_kill.extend(parent_map[curr_pid])
        return killed_process
