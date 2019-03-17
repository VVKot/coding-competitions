class Solution:
    def hasPathSum(self, root, sum):
        if not root:
            return False
        stack = [(root, root.val)]
        while stack:
            curr, curr_path = stack.pop()
            if not curr.left and not curr.right and curr_path == sum:
                return True
            if curr.left:
                stack.append((curr.left, curr_path + curr.left.val))
            if curr.right:
                stack.append((curr.right, curr_path + curr.right.val))
        return False