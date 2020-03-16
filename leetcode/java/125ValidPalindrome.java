/**
 * T: O(N) S: O(1)
 *
 * <p>Use two pointers, find first alphanumeric charaters from the left and from the right. If they
 * do not match - the string is not a palindrome. Otherwise, proceed to the next pair of
 * alphanumeric characters.
 */
class Solution {
  public boolean isPalindrome(String s) {
    int i = 0;
    int j = s.length() - 1;
    while (i < j) {
      if (!Character.isLetterOrDigit(s.charAt(i))) {
        i++;
        continue;
      }

      if (!Character.isLetterOrDigit(s.charAt(j))) {
        j--;
        continue;
      }
      char left = Character.toLowerCase(s.charAt(i));
      char right = Character.toLowerCase(s.charAt(j));
      if (left != right) {
        return false;
      }
      i++;
      j--;
    }
    return true;
  }
}
