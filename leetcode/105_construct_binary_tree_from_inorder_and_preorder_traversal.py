from typing import List, Optional


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    def buildTree(self,
                  preorder: List[int],
                  inorder: List[int]) -> Optional[TreeNode]:
        if not preorder:
            return None
        self.in_indices = {num: i for i, num in enumerate(inorder)}
        self.pre_index = 0
        return self.build_rec(0, len(preorder) - 1, preorder)

    def build_rec(self,
                  left: int,
                  right: int,
                  preorder: List[int]) -> TreeNode:
        val = preorder[self.pre_index]
        node = TreeNode(val)
        if left == right:
            return node
        inorder_index = self.in_indices[val]
        if left != inorder_index:
            self.pre_index += 1
            node.left = self.build_rec(left, inorder_index-1, preorder)

        if right != inorder_index:
            self.pre_index += 1
            node.right = self.build_rec(inorder_index+1, right, preorder)
        return node
