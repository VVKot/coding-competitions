/**
 * T: O(N) S: O(N)
 *
 * <p>Just do as the description says.
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
  public TreeNode invertTree(TreeNode root) {
    Deque<TreeNode> nodesToProcess = new LinkedList<>();
    nodesToProcess.add(root);
    while (!nodesToProcess.isEmpty()) {
      TreeNode currentNode = nodesToProcess.pop();
      if (currentNode == null) {
        continue;
      }
      TreeNode temp = currentNode.left;
      currentNode.left = currentNode.right;
      currentNode.right = temp;
      nodesToProcess.push(currentNode.left);
      nodesToProcess.push(currentNode.right);
    }
    return root;
  }
}
