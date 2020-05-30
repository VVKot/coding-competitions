import java.util.PriorityQueue;

class Solution {
  public int[][] kClosest(int[][] points, int K) {
    PriorityQueue<int[]> closestPoints =
        new PriorityQueue<int[]>(
            (p1, p2) -> p2[0] * p2[0] + p2[1] * p2[1] - p1[0] * p1[0] - p1[1] * p1[1]);
    for (int[] point : points) {
      closestPoints.offer(point);
      if (closestPoints.size() > K) {
        closestPoints.poll();
      }
    }
    return closestPoints.toArray(new int[K][2]);
  }
}
