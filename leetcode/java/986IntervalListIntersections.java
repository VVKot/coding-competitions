/**
 * T: O(A+B) S: O(A+B)
 *
 * <p>To check if there is an intersection we check if the bigger of starts is smaller than the
 * smaller of ends. If so - we found an intersection and add it to the result. In any case, we
 * advance the smaller interval. In the end we just return found intersetions.
 */
import java.util.ArrayList;
import java.util.List;

class Solution {
  public int[][] intervalIntersection(int[][] A, int[][] B) {
    List<int[]> intersections = new ArrayList();
    int a = 0;
    int b = 0;

    while (a < A.length && b < B.length) {
      int start = Math.max(A[a][0], B[b][0]);
      int end = Math.min(A[a][1], B[b][1]);
      if (start <= end) intersections.add(new int[] {start, end});

      if (A[a][1] < B[b][1]) a++;
      else b++;
    }

    return intersections.toArray(new int[intersections.size()][]);
  }
}
