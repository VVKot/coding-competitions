"""
T: O(N)
S: O(N)

We use stack to record last executed operation. If we have seen an operation Y
execute in the middle of operation X, this means X will continue at Y's end+1.
"""

from typing import List


class Solution:

    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        tasks = []  # type: List[List[int]]
        tasks_time = [0] * n
        for log in logs:
            task_str_id, operation, timestamp_str = log.split(':')
            task_id, timestamp = int(task_str_id), int(timestamp_str)
            if operation == 'start':
                if tasks:
                    prev_task, prev_timestamp = tasks[-1]
                    tasks_time[prev_task] += timestamp - prev_timestamp
                tasks.append([task_id, timestamp])
            else:
                prev_task, prev_timestamp = tasks.pop()
                tasks_time[prev_task] += timestamp - prev_timestamp + 1
                if tasks:
                    tasks[-1][1] = timestamp + 1
        return tasks_time
