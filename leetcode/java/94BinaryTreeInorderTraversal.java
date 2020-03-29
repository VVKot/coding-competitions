/**
 * T: O(N) S: O(N)
 *
 * Traverse the left subtree until the end on the each iteration. Start with the deepest left-most node and walk back
 * from it, visiting its parent and right child. */
import java.util.ArrayList;
import java.util.List;
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
  public List<Integer> inorderTraversal(TreeNode root) {
    List<Integer> traversedNodes = new ArrayList<>();
    Stack<TreeNode> nodesToProcess = new Stack<>();
    while (!nodesToProcess.isEmpty() || root != null) {
      while (root != null) {
        nodesToProcess.push(root);
        root = root.left;
      }
      TreeNode currentNode = nodesToProcess.pop();
      traversedNodes.add(currentNode.val);
      root = currentNode.right;
    }
    return traversedNodes;
  }
}
