/**
 * T: O(N**2) S: O(N**2)
 *
 * <p>The question is the same as LCS. Find the maximum result for current node from the calculation
 * for the previous one. If current node in bottom row does not match the node in the top row -
 * consider walking through both top and bottom row.
 */
class Solution {
  public int maxUncrossedLines(int[] A, int[] B) {
    int a = A.length;
    int b = B.length;
    int[][] dp = new int[a + 1][b + 1];
    for (int i = 1; i <= a; i++) {
      for (int j = 1; j <= b; j++) {
        if (A[i - 1] == B[j - 1]) {
          dp[i][j] = dp[i - 1][j - 1] + 1;
        } else {
          dp[i][j] = Math.max(dp[i - 1][j], dp[i][j - 1]);
        }
      }
    }
    return dp[a][b];
  }
}
