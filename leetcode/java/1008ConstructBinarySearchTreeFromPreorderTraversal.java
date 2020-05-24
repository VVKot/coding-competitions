/**
 * T: (N) S: O(N)
 *
 * <p>Process nodes one by one. When we see new node, we have to find appropriate parent for it - it
 * is the top most node that has value less than current one in case of new right child, or simply
 * last added node in case of new left child. After that, put the node to the appropriate property
 * of the parent and add it to the stack.
 */
import java.util.Deque;
import java.util.LinkedList;

public class TreeNode {
  int val;

  TreeNode left;
  TreeNode right;

  TreeNode(int x) {
    val = x;
  }
}

class Solution {
  public TreeNode bstFromPreorder(int[] preorder) {
    int numNodes = preorder.length;
    if (numNodes == 0) {
      return null;
    }
    Deque<TreeNode> existingNodes = new LinkedList<TreeNode>();
    TreeNode root = new TreeNode(preorder[0]);
    existingNodes.push(root);
    for (int i = 1; i < numNodes; i++) {
      TreeNode child = new TreeNode(preorder[i]);
      TreeNode parent = existingNodes.peek();
      while (!existingNodes.isEmpty() && existingNodes.peek().val < child.val) {
        parent = existingNodes.pop();
      }
      if (parent.val > child.val) {
        parent.left = child;
      } else {
        parent.right = child;
      }
      existingNodes.push(child);
    }
    return root;
  }
}
