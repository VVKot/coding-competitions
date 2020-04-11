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
  public int diameterOfBinaryTree(TreeNode root) {
    Map<TreeNode, Integer> nodeDepth = new HashMap<>();
    nodeDepth.put(null, 0);
    Stack<TreeNode> nodesToProcess = new Stack<>();
    nodesToProcess.push(root);
    int maxDiameter = 0;
    while (!nodesToProcess.isEmpty()) {
      TreeNode currentNode = nodesToProcess.pop();
      if (currentNode == null) {
        continue;
      }
      TreeNode left = currentNode.left;
      TreeNode right = currentNode.right;
      if (nodeDepth.containsKey(left) && nodeDepth.containsKey(right)) {
        int leftDepth = nodeDepth.get(left);
        int rightDepth = nodeDepth.get(right);
        maxDiameter = Math.max(maxDiameter, leftDepth + rightDepth);
        nodeDepth.put(currentNode, Math.max(leftDepth, rightDepth) + 1);
      } else {
        nodesToProcess.push(currentNode);
        nodesToProcess.push(right);
        nodesToProcess.push(left);
      }
    }
    return maxDiameter;
  }
}
