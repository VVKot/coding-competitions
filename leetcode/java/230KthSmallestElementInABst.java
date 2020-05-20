/**
 * T: O(N) S: O(N)
 *
 * <p>Perform inorder traversal, stop when we find the kth element. This is the answer since inorder
 * traversal of the BST is a sorted list of its values.
 */
import java.util.Deque;
import java.util.LinkedList;

public class TreeNode {
  int val;
  TreeNode left;
  TreeNode right;

  TreeNode() {}

  TreeNode(int val) {
    this.val = val;
  }

  TreeNode(int val, TreeNode left, TreeNode right) {
    this.val = val;
    this.left = left;
    this.right = right;
  }
}

class Solution {
  public int kthSmallest(TreeNode root, int k) {
    Deque<TreeNode> nodes = new LinkedList<>();
    while (true) {
      while (root != null) {
        nodes.push(root);
        root = root.left;
      }
      TreeNode currentNode = nodes.pop();
      k -= 1;
      if (k == 0) {
        return currentNode.val;
      }
      root = currentNode.right;
    }
  }
}
