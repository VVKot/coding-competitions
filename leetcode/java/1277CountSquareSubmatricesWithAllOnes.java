/**
 * T: O(R*C) S: O(1)
 *
 * <p>First, we find all squares that are formed at the particular point. If all of the left, top,
 * and topleft points form squares of size X, the current point forms X+1 squares. After that, we
 * just sum all of them.
 */
class Solution {
  public int countSquares(int[][] matrix) {
    int rows = matrix.length;
    int cols = rows == 0 ? 0 : matrix[0].length;
    for (int r = 1; r < rows; r++) {
      for (int c = 1; c < cols; c++) {
        if (matrix[r][c] == 1) {
          matrix[r][c] =
              Math.min(Math.min(matrix[r - 1][c], matrix[r][c - 1]), matrix[r - 1][c - 1]) + 1;
        }
      }
    }
    int squareCount = 0;
    for (int[] row : matrix) {
      for (int value : row) {
        squareCount += value;
      }
    }
    return squareCount;
  }
}
