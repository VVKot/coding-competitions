"""
T: O(N+M)
S: O(N+M) - additional

Do two inorder traversals in parallel. On each iteration select stack with the
minimum last element.
"""

from typing import List, Tuple


class TreeNode:

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        all_elements = []
        stack1, stack2 = [], []  # type: List[TreeNode], List[TreeNode]
        while any([root1, root2, stack1, stack2]):
            stack1, root1 = self.push_left(stack1, root1)
            stack2, root2 = self.push_left(stack2, root2)
            smallest_stack = self.get_smallest_stack(stack1, stack2)
            curr = smallest_stack.pop()
            all_elements.append(curr.val)
            if smallest_stack is stack1:
                root1 = curr.right
            else:
                root2 = curr.right
        return all_elements

    def push_left(self,
                  stack: List[TreeNode],
                  root: TreeNode) -> Tuple[List[TreeNode], TreeNode]:
        while root:
            stack.append(root)
            root = root.left
        return stack, root

    def get_smallest_stack(self,
                           stack1: List[TreeNode],
                           stack2: List[TreeNode]) -> List[TreeNode]:
        if stack1 and stack2:
            return stack1 if stack1[-1].val <= stack2[-1].val else stack2
        return stack1 or stack2
