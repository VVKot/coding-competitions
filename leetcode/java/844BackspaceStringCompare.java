/**
 * T: O(S+T) S: O(1)
 *
 * <p>Start from the end of the string and find non-backspace characters. Compare them and terminate
 * early if we go out of bounds for any of the strings.
 */
class Solution {
  public boolean backspaceCompare(String S, String T) {
    int i = S.length() - 1, j = T.length() - 1;
    while (i >= 0 || j >= 0) {
      i = this.findFirstNonBackspace(S, i);
      j = this.findFirstNonBackspace(T, j);
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

  private int findFirstNonBackspace(String S, int startingPosition) {
    int i = startingPosition;
    int backspaceCount = 0;
    while (i >= 0 && (S.charAt(i) == '#' || backspaceCount > 0)) {
      if (S.charAt(i) == '#') {
        backspaceCount += 1;
      } else {
        backspaceCount -= 1;
      }
      i -= 1;
    }
    return i;
  }
}
