class TreeNode:

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    def distributeCoins(self, root: TreeNode) -> int:
        self.result = 0
        _ = self.move_coins(root)
        return self.result

    def move_coins(self, root: TreeNode) -> int:
        if not root:
            return 0
        left_coins_to_move = self.move_coins(root.left)
        right_coins_to_move = self.move_coins(root.right)
        self.result += abs(left_coins_to_move) + abs(right_coins_to_move)
        return left_coins_to_move + right_coins_to_move + root.val - 1
