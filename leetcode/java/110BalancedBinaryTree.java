/**
 * T: O(N) S: O(N)
 *
 * <p>Traverse the tree, get depth of left and right children. If the current subtree is unbalanced
 * or left or right subtree is unbalanced - mark current subtree as unbalanced. Otherwise, record
 * the real maximum depth of the current subtree - depth of the deeper child(left or right) plus
 * one. This way, if any subtree is unbalanced - this information will be propagated to the root.
 */
import java.util.HashMap;
import java.util.Map;
import java.util.Stack;

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
    Map<TreeNode, Integer> nodeDepths = new HashMap<>();
    nodeDepths.put(null, 0);
    Stack<TreeNode> nodesToProcess = new Stack<>();
    nodesToProcess.push(root);
    while (!nodesToProcess.isEmpty()) {
      TreeNode currentNode = nodesToProcess.pop();
      if (currentNode == null) {
        continue;
      }
      TreeNode left = currentNode.left;
      TreeNode right = currentNode.right;
      if (nodeDepths.containsKey(left) && nodeDepths.containsKey(right)) {
        int leftDepth = nodeDepths.get(left);
        int rightDepth = nodeDepths.get(right);
        if (leftDepth == DEPTH_OF_UNBALANCED_TREE
            || rightDepth == DEPTH_OF_UNBALANCED_TREE
            || Math.abs(leftDepth - rightDepth) > 1) {
          nodeDepths.put(currentNode, DEPTH_OF_UNBALANCED_TREE);
        } else {
          nodeDepths.put(currentNode, Math.max(leftDepth, rightDepth) + 1);
        }
      } else {
        nodesToProcess.push(currentNode);
        nodesToProcess.push(right);
        nodesToProcess.push(left);
      }
    }
    return nodeDepths.get(root) != DEPTH_OF_UNBALANCED_TREE;
  }
}
