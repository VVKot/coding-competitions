/**
 * T: O(M*N) S: O(M*N)
 *
 * <p>On each step we check what the maximum square that can be made of the left, top, and top left
 * of the current cell. If on all of them we can make a square of size S, we can make a square of
 * size S+1 on the current cell.
 */
class Solution {
  public int maximalSquare(char[][] matrix) {
    int rows = matrix.length;
    int cols = rows == 0 ? 0 : matrix[0].length;
    int[][] dp = new int[rows + 1][cols + 1];
    int maxSide = 0;
    for (int r = 1; r <= rows; r++) {
      for (int c = 1; c <= cols; c++) {
        if (matrix[r - 1][c - 1] == '1') {
          dp[r][c] = Math.min(Math.min(dp[r - 1][c], dp[r][c - 1]), dp[r - 1][c - 1]) + 1;
          maxSide = Math.max(maxSide, dp[r][c]);
        }
      }
    }
    return maxSide * maxSide;
  }
}
