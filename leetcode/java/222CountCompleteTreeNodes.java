class Solution {
  public int computeDepth(TreeNode node) {
    int depth = 0;
    while (node.left != null) {
      node = node.left;
      depth++;
    }
    return depth;
  }

  public boolean exists(int idx, int depth, TreeNode node) {
    int left = 0;
    int right = (int)Math.pow(2, depth) - 1;
    int pivot = 0;
    for(int i = 0; i < depth; ++i) {
      pivot = left + (right - left) / 2;
      if (idx <= pivot) {
        node = node.left;
        right = pivot;
      }
      else {
        node = node.right;
        left = pivot + 1;
      }
    }
    return node != null;
  }

  public int countNodes(TreeNode root) {
    if (root == null) { return 0;
    }
    int depth = computeDepth(root);
    if (depth == 0) { return 1; }

    int left = 1;
    int right = (int)Math.pow(2, depth) - 1;
    int pivot = 0;
    while (left <= right) {
      pivot = left + (right - left) / 2;
      if (exists(pivot, depth, root)) { left = pivot + 1;
      }      else { right = pivot - 1;
      }    }

    return (int)Math.pow(2, depth) - 1 + left;
  }
}
