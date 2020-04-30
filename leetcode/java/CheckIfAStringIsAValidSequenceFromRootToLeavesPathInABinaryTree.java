import java.util.LinkedList;
import java.util.Queue;

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
  public boolean isValidSequence(TreeNode root, int[] arr) {
    Queue<TreeNode> nodesToProcess = new LinkedList<>();
    nodesToProcess.offer(root);
    for (int depth = 0; !nodesToProcess.isEmpty() && depth < arr.length; depth++) {
      for (int size = nodesToProcess.size(); size > 0; size--) {
        TreeNode currentNode = nodesToProcess.poll();
        if (currentNode != null && currentNode.val == arr[depth]) {
          if (depth == arr.length - 1 && currentNode.left == null && currentNode.right == null) {
            return true;
          }
          nodesToProcess.offer(currentNode.left);
          nodesToProcess.offer(currentNode.right);
        }
      }
    }
    return false;
  }
}
