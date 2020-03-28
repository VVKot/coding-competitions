/**
 * T: O(N) S: O(N)
 *
 * <p>Traverse the tree, get depth of left and right children. If the current subtree is unbalanced
 * or left or right subtree is unbalanced - return constant indicating unbalanced subtree.
 * Otherwise, return the maximum depth of the current subtree. This way, if any subtree is
 * unbalanced - this information will be propagated to the root.
 */
public class TreeNode {
  int val;
  TreeNode left;
  TreeNode right;

  TreeNode(int x) {
    val = x;
  }
}

class Solution {
  private final int DEPTH_OF_UNBALANCED_TREE = -1;

  public boolean isBalanced(TreeNode root) {
    return getDepth(root) != DEPTH_OF_UNBALANCED_TREE;
  }

  private int getDepth(TreeNode node) {
    if (node == null) {
      return 0;
    }
    int left = getDepth(node.left);
    int right = getDepth(node.right);
    if (left == DEPTH_OF_UNBALANCED_TREE
        || right == DEPTH_OF_UNBALANCED_TREE
        || Math.abs(left - right) > 1) {
      return DEPTH_OF_UNBALANCED_TREE;
    }
    return Math.max(left, right) + 1;
  }
}
