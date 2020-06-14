import java.util.Arrays;
import java.util.PriorityQueue;
import java.util.Queue;

class Solution {
  public int findCheapestPrice(int n, int[][] flights, int src, int dst, int K) {
    int adjMatrix[][] = new int[n][n];
    for (int[] flight : flights) {
      adjMatrix[flight[0]][flight[1]] = flight[2];
    }

    int[] distances = new int[n];
    int[] currentStops = new int[n];
    Arrays.fill(distances, Integer.MAX_VALUE);
    Arrays.fill(currentStops, Integer.MAX_VALUE);
    distances[src] = 0;
    currentStops[src] = 0;

    Queue<int[]> minHeap = new PriorityQueue<int[]>((a, b) -> a[1] - b[1]);
    minHeap.offer(new int[] {src, 0, 0});

    while (!minHeap.isEmpty()) {
      int[] info = minHeap.poll();
      int node = info[0], stops = info[2], cost = info[1];
      if (node == dst) {
        return cost;
      }
      if (stops == K + 1) {
        continue;
      }
      for (int nei = 0; nei < n; nei++) {
        if (adjMatrix[node][nei] > 0) {
          int dU = cost;
          int dV = distances[nei];
          int wUV = adjMatrix[node][nei];
          if (dU + wUV < dV) {
            minHeap.offer(new int[] {nei, dU + wUV, stops + 1});
            distances[nei] = dU + wUV;
          } else if (stops < currentStops[nei]) {
            minHeap.offer(new int[] {nei, dU + wUV, stops + 1});
            currentStops[nei] = stops;
          }
        }
      }
    }

    return distances[dst] == Integer.MAX_VALUE ? -1 : distances[dst];
  }
}
