/**
 * T: O(N) S: O(1)
 *
 * <p>Two points always form a line. Three points form a line if slope of the line between first and
 * second is the same as the slope between second and third. Since this property is associative, we
 * can expand that to arbitrarily many points by moving one point at a time and checking the last
 * three points to see if it still holds.
 */
class Solution {
  public boolean checkStraightLine(int[][] coordinates) {
    if (coordinates.length == 2) {
      return true;
    }
    for (int i = 0; i < coordinates.length - 2; i++) {
      if (!arePointsOnTheSameLine(coordinates, i)) {
        return false;
      }
    }
    return true;
  }

  private boolean arePointsOnTheSameLine(int[][] coordinates, int i) {
    int[] point0 = coordinates[i];
    int[] point1 = coordinates[i + 1];
    int[] point2 = coordinates[i + 2];
    int x0 = point0[0];
    int y0 = point0[1];
    int x1 = point1[0];
    int y1 = point1[1];
    int x2 = point2[0];
    int y2 = point2[1];
    return (x1 - x0) * (y2 - y1) == (x2 - x1) * (y1 - y0);
  }
}
