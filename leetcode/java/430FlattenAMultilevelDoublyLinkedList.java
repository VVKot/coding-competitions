import java.util.ArrayDeque;
import java.util.Deque;

class Node {
  public int val;
  public Node prev;
  public Node next;
  public Node child;

  public Node() {}

  public Node(int _val, Node _prev, Node _next, Node _child) {
    val = _val;
    prev = _prev;
    next = _next;
    child = _child;
  }
};

class Solution {
  public Node flatten(Node head) {
    if (head == null) return head;

    Node pseudoHead = new Node(0, null, head, null);
    Node curr, prev = pseudoHead;

    Deque<Node> stack = new ArrayDeque<>();
    stack.push(head);

    while (!stack.isEmpty()) {
      curr = stack.pop();
      prev.next = curr;
      curr.prev = prev;

      if (curr.next != null) stack.push(curr.next);
      if (curr.child != null) {
        stack.push(curr.child);
        curr.child = null;
      }
      prev = curr;
    }
    pseudoHead.next.prev = null;
    return pseudoHead.next;
  }
}
