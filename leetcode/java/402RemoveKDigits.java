/**
 * T: O(N) S: O(N)
 *
 * <p>Traverse the input number and greedely remove the highest leftmost character if we are still
 * allowed to do so. If we are still have digits to remove after the traversal, we remove from the
 * right, since at this point all of the digits in the stack are in non-decreasing order.
 */
import java.util.LinkedList;

class Solution {
  private static final String ZERO = "0";
  private static final char ZERO_CHAR = '0';

  public String removeKdigits(String num, int k) {
    LinkedList<Character> resultingDigits = new LinkedList<>();
    for (char digit : num.toCharArray()) {
      while (!resultingDigits.isEmpty() && k > 0 && resultingDigits.peekLast() > digit) {
        resultingDigits.pollLast();
        k--;
      }
      resultingDigits.offerLast(digit);
    }
    for (int i = 0; i < k; i++) {
      resultingDigits.pollLast();
    }
    StringBuilder result = new StringBuilder();
    boolean maybeHasLeadingZero = true;
    for (char digit : resultingDigits) {
      if (maybeHasLeadingZero && digit == ZERO_CHAR) {
        continue;
      }
      maybeHasLeadingZero = false;
      result.append(digit);
    }
    if (result.length() == 0) {
      return ZERO;
    }
    return result.toString();
  }
}
