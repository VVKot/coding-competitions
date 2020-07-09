import java.util.HashMap;
import java.util.Map;

class Solution {
  private int maxWidth = 0;
  private Map<Integer, Integer> firstColIndexTable;

  protected void DFS(TreeNode node, Integer depth, Integer colIndex) {
    if (node == null) {
      return;
    }
    if (!firstColIndexTable.containsKey(depth)) {
      firstColIndexTable.put(depth, colIndex);
    }
    int firstColIndex = firstColIndexTable.get(depth);
    maxWidth = Math.max(this.maxWidth, colIndex - firstColIndex + 1);

    DFS(node.left, depth + 1, 2 * colIndex);
    DFS(node.right, depth + 1, 2 * colIndex + 1);
  }

  public int widthOfBinaryTree(TreeNode root) {
    this.firstColIndexTable = new HashMap<Integer, Integer>();
    DFS(root, 0, 0);
    return this.maxWidth;
  }
}
