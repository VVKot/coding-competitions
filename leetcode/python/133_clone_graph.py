class Node:

    def __init__(self, val, neighbors):
        self.val = val
        self.neighbors = neighbors


class Solution:

    def cloneGraph(self, node: Node) -> Node:
        cloned = Node(node.val, [])
        mapping = {node: cloned}
        stack = [node]
        while stack:
            curr = stack.pop()
            for neigh in curr.neighbors:
                if neigh not in mapping:
                    cloned = Node(neigh.val, [])
                    mapping[neigh] = cloned
                    stack.append(neigh)
                mapping[curr].neighbors.append(mapping[neigh])
        return mapping[node]
