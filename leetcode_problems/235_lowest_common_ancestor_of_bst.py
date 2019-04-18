class Solution:
    def lowestCommonAncestor(self, root, p, q):
        small, big = sorted([p.val, q.val])
        while not small <= root.val <= big:
            if small > root.val:
                root = root.right
            else:
                root = root.left
        return root
