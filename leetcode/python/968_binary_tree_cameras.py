class TreeNode:

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    def minCameraCover(self, root: TreeNode) -> int:
        self.camera_count = 0
        cover = set([None])

        def dfs(node, parent):
            if node:
                dfs(node.left, node)
                dfs(node.right, node)

                if (not parent and node not in cover) or \
                        (node.left not in cover or node.right not in cover):
                    self.camera_count += 1
                    for to_cover in (parent, node, node.left, node.right):
                        cover.add(to_cover)
        dfs(root, None)
        return self.camera_count
