class Solution {
  public int preorder(TreeNode node, int currNumber) {
    if (node != null) {
      currNumber = currNumber * 10 + node.val;
      if (node.left == null && node.right == null) {
        return currNumber;
      }
      return preorder(node.left, currNumber) + preorder(node.right, currNumber);
    }
    return 0;
  }

  public int sumNumbers(TreeNode root) {
    return preorder(root, 0);
  }
}
