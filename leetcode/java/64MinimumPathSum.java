/**
 * T: O(R*C) S: O(1)
 *
 * <p>The minimum sum to reach each grid cell is determinted by the minimum sum to reach either cell
 * to the top or to the left of it. This is true only in this specific case because all cells are
 * guaranteed to have non-negative values. Due to that, we can greedily calculate the sum of the
 * path to the specific cell.
 */
class Solution {
  public int minPathSum(int[][] grid) {
    if (grid.length == 0) {
      return 0;
    }
    int rowCount = grid.length;
    int colCount = grid[0].length;
    for (int r = 0; r < rowCount; r++) {
      for (int c = 0; c < colCount; c++) {
        if (r == 0 && c == 0) {
          continue;
        }
        int top = r == 0 ? Integer.MAX_VALUE : grid[r - 1][c];
        int left = c == 0 ? Integer.MAX_VALUE : grid[r][c - 1];
        grid[r][c] += Math.min(top, left);
      }
    }
    return grid[rowCount - 1][colCount - 1];
  }
}
