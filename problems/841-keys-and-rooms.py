class Solution:
    def canVisitAllRooms(self, rooms):
        stack = [0]
        visited = set(stack)
        while stack:
            curr = stack.pop()
            for room in rooms[curr]:
                if room not in visited:
                    stack.append(room)
                    visited.add(room)
                    if len(visited) == len(rooms): return True
        return len(visited) == len(rooms)