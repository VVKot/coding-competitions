class TreeNode:

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    def twoSumBSTs(self,
                   root1: TreeNode,
                   root2: TreeNode,
                   target: int) -> bool:
        min_stack, max_stack = [], []
        while True:
            while root1:
                min_stack.append(root1)
                root1 = root1.left
            while root2:
                max_stack.append(root2)
                root2 = root2.right
            if not min_stack or not max_stack:
                return False
            min_node, max_node = min_stack[-1], max_stack[-1]
            total = min_node.val + max_node.val
            if total == target:
                return True
            if total < target:
                too_small = min_stack.pop()
                root1 = too_small.right
            else:
                too_large = max_stack.pop()
                root2 = too_large.left
