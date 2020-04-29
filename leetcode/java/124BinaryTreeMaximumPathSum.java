/**
 * T: O(N) S: O(N)
 *
 * <p>We visit each node and check what's the maximum path through it. We update the global maximum
 * path and return the maximum pass through the current node using only one branch in case it is a
 * part of path with a greater sum.
 */
import java.util.ArrayList;
import java.util.Collections;

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
  private int globalMax = Integer.MIN_VALUE;

  public int maxPathSum(TreeNode root) {
    helper(root);

    return globalMax;
  }

  private int helper(TreeNode node) {
    if (node == null) {
      return Integer.MIN_VALUE;
    }
    int left = helper(node.left);
    int right = helper(node.right);
    ArrayList<Integer> pathSums = new ArrayList<>();
    pathSums.add(node.val);
    if (left > 0) {
      pathSums.add(node.val + left);
    }
    if (right > 0) {
      pathSums.add(node.val + right);
    }
    int maxOneBranchPath = Collections.max(pathSums);

    if (left > 0 && right > 0) {
      pathSums.add(node.val + left + right);
    }
    int maxTwoBranchPath = Collections.max(pathSums);
    globalMax = Math.max(globalMax, maxTwoBranchPath);

    return maxOneBranchPath;
  }
}
