/**
 * T: O(N) S: O(N)
 *
 * <p>Use iteration - traverse the current node first and then all of its children afterwards, from
 * first to last. To achieve that we need to push them to the stack in reverse order.
 */
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.Stack;

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
    List<Integer> preorderTraversal = new ArrayList<>();
    Stack<Node> nodesToProcess = new Stack<Node>() {};
    nodesToProcess.push(root);
    while (!nodesToProcess.isEmpty()) {
      Node currentNode = nodesToProcess.pop();
      if (currentNode != null) {
        preorderTraversal.add(currentNode.val);
        Collections.reverse(currentNode.children);
        for (Node child : currentNode.children) {
          nodesToProcess.add(child);
        }
      }
    }
    return preorderTraversal;
  }
}
