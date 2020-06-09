/**
 * T: O(S+T) S: O(1)
 *
 * <p>Walk through S and S simultaneously, check the current character. If they match, we can
 * advance through S. If in the end we have walked through all of the S - it is a subsequence.
 */
class Solution {
  public boolean isSubsequence(String s, String t) {
    int i = 0;
    int j = 0;
    while (i < s.length() && j < t.length()) {
      if (s.charAt(i) == t.charAt(j)) {
        i++;
      }
      j++;
    }
    return i == s.length();
  }
}
