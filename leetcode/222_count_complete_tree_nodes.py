class TreeNode:

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    def countNodes(self, root: TreeNode) -> int:
        node_count = 0
        if not root:
            return node_count
        depth = self.get_depth(root)
        node_count += 2 ** depth - 1
        last_node_index = 0
        left, right = 0, 2 ** depth - 1
        while left <= right:
            mid = (left+right) // 2
            at_mid = self.is_leaf_exists(root, depth, mid)
            if at_mid:
                last_node_index = mid
                left = mid+1
            else:
                right = mid-1
        return node_count + last_node_index + 1

    def get_depth(self, root: TreeNode) -> int:
        depth = 0
        while root and root.left:
            depth += 1
            root = root.left
        return depth

    def is_leaf_exists(self,
                       root: TreeNode,
                       depth: int,
                       index: int) -> bool:
        left, right = 0, 2 ** depth - 1
        for _ in range(depth):
            mid = (left+right) // 2
            if index <= mid:
                root = root.left
                right = mid
            else:
                root = root.right
                left = mid+1
        return root is not None
