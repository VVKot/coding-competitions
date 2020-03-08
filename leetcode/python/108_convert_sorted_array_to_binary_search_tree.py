"""
T: O(N)
S: O(N)

Iterative implementation of the recursive idea. We do only one path since we
remember the parent and which direction(left or right) we went. The only thing
left is to record the reference to the head.
"""

from typing import List, Optional, Tuple


class TreeNode:

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        start, end = 0, len(nums) - 1
        nums_to_proceses = [
            (start, end, None, False)
        ]  # type: List[Tuple[int, int, Optional[TreeNode], bool]]
        head = None
        while nums_to_proceses:
            left, right, prev, is_left = nums_to_proceses.pop()
            if left > right:
                continue
            mid = (left + right) // 2
            curr = TreeNode(nums[mid])
            if prev:
                if is_left:
                    prev.left = curr
                else:
                    prev.right = curr
            else:
                head = curr
            nums_to_proceses.append((left, mid - 1, curr, True))
            nums_to_proceses.append((mid + 1, right, curr, False))
        return head
