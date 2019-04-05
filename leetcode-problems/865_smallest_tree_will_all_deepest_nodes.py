class Solution:
    def get_depth(self, root):
        if not root:
            return 0, None
        left, left_root = self.get_depth(root.left)
        right, right_root = self.get_depth(root.right)
        if left > right:
            return left + 1, left_root
        elif left < right:
            return right + 1, right_root
        else:
            return left + 1, root

    def subtreeWithAllDeepest(self, root):
        _, result = self.get_depth(root)
        return result
