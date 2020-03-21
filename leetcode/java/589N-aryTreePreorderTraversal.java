/**
 * T: O(N) S: O(N)
 *
 * <p>Use recursion - traverse the current node first and then all of its children afterwards, from
 * first to last.
 */
import java.util.ArrayList;
import java.util.List;

class Node {
  public int val;
  public List<Node> children;

  public Node() {}

  public Node(final int _val) {
    val = _val;
  }

  public Node(final int _val, final List<Node> _children) {
    val = _val;
    children = _children;
  }
}

class Solution {
  public List<Integer> preorder(final Node root) {
    if (root == null) {
      return new ArrayList<>();
    }
    List<Integer> preorderTraversal = new ArrayList<>();
    preorderTraversal.add(root.val);
    for (Node child : root.children) {
      preorderTraversal.addAll(preorder(child));
    }
    return preorderTraversal;
  }
}
