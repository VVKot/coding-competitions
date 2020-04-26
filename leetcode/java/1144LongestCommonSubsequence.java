/**
 * T: O(M*N) S: O(M*N)
 *
 * <p>Each node in the DP matrix represent the LCS for the i's character of text1 and j's character
 * of text2. We process characters one by one and if they are similar - we now we can built an LCS
 * of length 1 + whatever is left starting from i+1 and j+1. If the charaters are different - we
 * take the LCS from either i+1 or j+1.
 */
class Solution {
  public int longestCommonSubsequence(String text1, String text2) {
    int[][] dp = new int[text1.length() + 1][text2.length() + 1];
    for (int r = text1.length() - 1; r >= 0; r--) {
      for (int c = text2.length() - 1; c >= 0; c--) {
        if (text1.charAt(r) == text2.charAt(c)) {
          dp[r][c] = 1 + dp[r + 1][c + 1];
        } else {
          dp[r][c] = Math.max(dp[r + 1][c], dp[r][c + 1]);
        }
      }
    }
    return dp[0][0];
  }
}
