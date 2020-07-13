import java.util.ArrayDeque;
import java.util.Deque;

class Solution {
  public boolean check(TreeNode p, TreeNode q) {
    if (p == null && q == null) {
      return true;
    }
    if (q == null || p == null) {
      return false;
    }
    if (p.val != q.val) {
      return false;
    }
    return true;
  }

  public boolean isSameTree(TreeNode p, TreeNode q) {
    if (p == null && q == null) {
      return true;
    }
    if (!check(p, q)) {
      return false;
    }
    Deque<TreeNode> deqP = new ArrayDeque<TreeNode>();
    Deque<TreeNode> deqQ = new ArrayDeque<TreeNode>();
    deqP.addLast(p);
    deqQ.addLast(q);

    while (!deqP.isEmpty()) {
      p = deqP.removeFirst();
      q = deqQ.removeFirst();

      if (!check(p, q)) {
        return false;
      }
      if (p != null) {
        if (!check(p.left, q.left)) {
          return false;
        }
        if (p.left != null) {
          deqP.addLast(p.left);
          deqQ.addLast(q.left);
        }
        if (!check(p.right, q.right)) {
          return false;
        }
        if (p.right != null) {
          deqP.addLast(p.right);
          deqQ.addLast(q.right);
        }
      }
    }
    return true;
  }
}
