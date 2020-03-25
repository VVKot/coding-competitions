/**
 * T: O(S+T) S: O(1)
 *
 * <p>Start from the end of the string and find non-backspace characters. Compare them and terminate
 * early if we go out of bounds for any of the strings.
 */
class Solution {
  public boolean backspaceCompare(String S, String T) {
    int i = S.length() - 1, j = T.length() - 1;
    int countS = 0, countT = 0;
    while (i >= 0 || j >= 0) {
      while (i >= 0 && (S.charAt(i) == '#' || countS > 0)) {
        if (S.charAt(i) == '#') {
          countS += 1;
        } else {
          countS -= 1;
        }
        i -= 1;
      }

      while (j >= 0 && (T.charAt(j) == '#' || countT > 0)) {
        if (T.charAt(j) == '#') {
          countT += 1;
        } else {
          countT -= 1;
        }
        j -= 1;
      }

      if (i < 0 || j < 0) {
        return i == j;
      }

      if (S.charAt(i) != T.charAt(j)) {
        return false;
      }
      i -= 1;
      j -= 1;
    }
    return i == j;
  }
}
