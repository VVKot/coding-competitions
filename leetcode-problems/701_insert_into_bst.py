class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None


class Solution:
	def insertIntoBST(self, root, val):
		if not root:
			return TreeNode(val)
		head = root
		while True:
			if val > head.val:
				if head.right:
					head=head.right
				else:
					head.right = TreeNode(val)
					break
			else:
				if head.left:
					head = head.left
				else:
					head.left = TreeNode(val)
					break
		return root

		
