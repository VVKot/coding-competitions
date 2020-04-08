/**
 * T: O(N) S: O(1)
 *
 * <p>Move two pointers, one at the normal speed, another one at the double speed. When the latter
 * reaches the end of the list - the former one points to the middle.
 */
public class ListNode {
  int val;
  ListNode next;

  ListNode(int x) {
    val = x;
  }
}

class Solution {
  public ListNode middleNode(ListNode head) {
    ListNode fast = head;
    ListNode slow = head;
    while (fast != null && fast.next != null) {
      fast = fast.next.next;
      slow = slow.next;
    }
    return slow;
  }
}
