from collections import deque


class Solution:
    def isEscapePossible(self, blocked, source, target):
        if not blocked:
            return True
        blocked = {(x, y) for x, y in blocked}
        source = tuple(source)
        target = tuple(target)

        def bfs(s, e):
            visited = {s}
            q = deque([s])
            while q:
                if len(q) > len(blocked):
                    return 1
                y, x = q.popleft()
                if (y, x) == e:
                    return 2
                for r, c in [(y-1, x), (y+1, x), (y, x-1), (y, x+1)]:
                    if (r, c) in visited or (r, c) in blocked:
                        continue
                    if 0 <= r < 10e6 and 0 <= c < 10e6:
                        visited.add((r, c))
                        q.append((r, c))
            return 0
        return bfs(source, target) + bfs(target, source) > 1
