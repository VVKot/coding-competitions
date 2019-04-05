class Solution:
    def isSameTree(self, p, q):
        if not p:
            if q:
                return False
            else:
                return True
        else:
            if not q:
                return False
        if p.val != q.val:
            return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
