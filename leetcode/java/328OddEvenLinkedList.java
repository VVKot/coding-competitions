/**
 * T: O(N) S: O(1)
 *
 * <p>First, we check if we can advance further. If so - next odd is after the current even, after
 * that - the new even is after the updated odd. We have to check for the even in the condition so
 * that we don't advance the latest odd to null, which will fail the last step - joining last odd to
 * the first even.
 */
public class ListNode {
  int val;
  ListNode next;

  ListNode() {}

  ListNode(int val) {
    this.val = val;
  }

  ListNode(int val, ListNode next) {
    this.val = val;
    this.next = next;
  }
}

class Solution {
  public ListNode oddEvenList(ListNode head) {
    if (head == null) {
      return null;
    }
    ListNode firstEven = head.next;
    ListNode currOdd = head;
    ListNode currEven = firstEven;
    while (currEven != null && currEven.next != null) {
      currOdd.next = currEven.next;
      currOdd = currOdd.next;
      currEven.next = currOdd.next;
      currEven = currEven.next;
    }
    currOdd.next = firstEven;
    return head;
  }
}
