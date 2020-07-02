import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

class Solution {
  public List<List<Integer>> levelOrderBottom(TreeNode root) {
    List<List<Integer>> nodesLevels = new ArrayList<List<Integer>>();
    if (root == null) {
      return nodesLevels;
    }

    ArrayDeque<TreeNode> currentLevel = new ArrayDeque<>();
    ArrayDeque<TreeNode> nextLevel =
        new ArrayDeque<>() {
          {
            offer(root);
          }
        };

    while (!nextLevel.isEmpty()) {
      currentLevel = nextLevel.clone();
      nextLevel.clear();
      nodesLevels.add(new ArrayList<Integer>());

      for (TreeNode node : currentLevel) {
        nodesLevels.get(nodesLevels.size() - 1).add(node.val);
        if (node.left != null) nextLevel.offer(node.left);
        if (node.right != null) nextLevel.offer(node.right);
      }
    }

    Collections.reverse(nodesLevels);
    return nodesLevels;
  }
}
