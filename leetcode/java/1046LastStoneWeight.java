/**
 * T: O(NlogN) S: O(NlogN)
 *
 * <p>Just perform actions specified by the description. Priority queue makes the implementation
 * faster compared to naive quadratic implementation.
 */
import java.util.Comparator;
import java.util.PriorityQueue;

class Solution {
  public int lastStoneWeight(int[] stones) {
    PriorityQueue<Integer> weightedStones =
        new PriorityQueue<>(Comparator.reverseOrder());
    for (int stone : stones) {
      weightedStones.offer(stone);
    }
    while (weightedStones.size() >= 2) {
      int stone1 = weightedStones.poll();
      int stone2 = weightedStones.poll();
      if (stone1 != stone2) {
        weightedStones.offer(stone1 - stone2);
      }
    }
    return weightedStones.isEmpty() ? 0 : weightedStones.peek();
  }
}
