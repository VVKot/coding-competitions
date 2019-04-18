# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def dfsBST(self, root, sum_so_far=0):
        if not root:
            return sum_so_far
        root.val += self.dfsBST(root.right, sum_so_far)
        return self.dfsBST(root.left, root.val)

    def convertBST(self, root):
        self.dfsBST(root)
        return root
