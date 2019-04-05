class Solution:
    def binaryTreePaths(self, root):
        if not root:
            return []
        result = []
        stack = [(root, str(root.val))]
        while stack:
            curr, path = stack.pop()
            if not curr.left and not curr.right:
                result.append(path)
            else:
                if curr.left:
                    new_path = "{}->{}".format(path, curr.left.val)
                    stack.append((curr.left, new_path))
                if curr.right:
                    new_path = "{}->{}".format(path, curr.right.val)
                    stack.append((curr.right, new_path))
        return result
