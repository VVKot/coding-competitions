class Solution:
    def searchBST(self, root, val):
        if not root:
            return None
        while root and val != root.val:
            if val < root.val:
                root = root.left
            elif val > root.val:
                root = root.right
        return root
