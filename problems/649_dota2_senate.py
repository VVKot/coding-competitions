from collections import deque


class Solution:
    def predictPartyVictory(self, senate):
        r_queue = deque()
        d_queue = deque()
        n = len(senate)
        for i, curr in enumerate(senate):
            if curr == 'R':
                r_queue.append(i)
            else:
                d_queue.append(i)
        while r_queue and d_queue:
            r_curr, d_curr = r_queue.popleft(), d_queue.popleft()
            if r_curr < d_curr:
                r_queue.append(r_curr + n)
            else:
                d_queue.append(d_curr + n)
        return "Radiant" if r_queue else "Dire"
