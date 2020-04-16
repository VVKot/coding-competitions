/*
 * T: O(N) S: O(1)
 *
 * Traverse string in both directions. During each iteration check if we have enough stars to account for the imbalance.
 * If we do for both left and right traversal - the string is valid.
 */

class Solution {
  public boolean checkValidString(String s) {
    int balance = 0;
    int starCount = 0;
    char[] chars = s.toCharArray();
    for (char ch : chars) {
      if (ch == '(') {
        balance -= 1;
      } else if (ch == ')') {
        balance += 1;
      } else {
        starCount += 1;
      }
      if (balance > starCount) {
        return false;
      }
    }
    balance = 0;
    starCount = 0;

    for (int i = chars.length - 1; i >= 0; i--) {
      char ch = chars[i];
      if (ch == '(') {
        balance += 1;
      } else if (ch == ')') {
        balance -= 1;
      } else {
        starCount += 1;
      }
      if (balance > starCount) {
        return false;
      }
    }
    return true;
  }
}
