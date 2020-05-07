/**
 * T: O(N) S: O(N)
 *
 * <p>We traverse the tree level by level keeping track of which node belongs to which parent. If we
 * find a matching node, we check if we have already seen possible cousin. If not - we just record
 * current node level and parent, otherwise we just compare current node to the seen one. We use
 * early stopping to not traverse the tree if we found of the possible cousins, since if another one
 * is deeper - we already know it is not a cousin.
 */
import java.util.ArrayDeque;
import java.util.Deque;
import java.util.HashMap;
import java.util.Map;

public class TreeNode {
  int val;
  TreeNode left;
  TreeNode right;

  TreeNode(int x) {
    val = x;
  }
}

class Solution {
  public boolean isCousins(TreeNode root, int x, int y) {
    TreeNode foundParent = null;
    int foundLevel = -1;

    int level = 0;
    Deque<TreeNode> nodesToProcess = new ArrayDeque<TreeNode>() {};
    nodesToProcess.offer(root);
    Map<TreeNode, TreeNode> nodeToParent = new HashMap<>();
    nodeToParent.put(root, null);
    while (!nodesToProcess.isEmpty()) {
      int currentLevelSize = nodesToProcess.size();
      for (int i = 0; i < currentLevelSize; i++) {
        TreeNode currentNode = nodesToProcess.poll();
        if (currentNode == null) {
          continue;
        }
        if (currentNode.val == x || currentNode.val == y) {
          if (foundParent == null) {
            foundParent = nodeToParent.get(currentNode);
            foundLevel = level;
          } else {
            return foundLevel == level && nodeToParent.get(currentNode) != foundParent;
          }
        } else {
          if (currentNode.left != null) {
            nodeToParent.put(currentNode.left, currentNode);
            nodesToProcess.offer(currentNode.left);
          }
          if (currentNode.right != null) {
            nodesToProcess.offer(currentNode.right);
            nodeToParent.put(currentNode.right, currentNode);
          }
        }
      }
      level++;
    }
    return false;
  }
}
