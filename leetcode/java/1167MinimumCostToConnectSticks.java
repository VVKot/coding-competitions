/**
 * T: O(NlogN) S: O(N)
 *
 * <p>Take two smallest sticks on each iteration to minimize cost. Use priority queue to make
 * complexity logarithmic instead of square.
 */
import java.util.Arrays;
import java.util.List;
import java.util.PriorityQueue;
import java.util.Queue;
import java.util.stream.Collectors;

class Solution {
  public int connectSticks(int[] sticks) {
    List<Integer> sticksList = Arrays.stream(sticks).boxed().collect(Collectors.toList());
    Queue<Integer> sortedSticks = new PriorityQueue<>(sticksList);
    int totalConnectingCost = 0;
    while (sortedSticks.size() > 1) {
      int smallestStick = sortedSticks.poll();
      int secondSmallestStick = sortedSticks.poll();
      int newStick = smallestStick + secondSmallestStick;
      totalConnectingCost += newStick;
      sortedSticks.offer(newStick);
    }
    return totalConnectingCost;
  }
}
