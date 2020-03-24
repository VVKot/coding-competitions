/**
 * T: O(N) S: O(N)
 *
 * <p>Find the modulo of the current number and look for the number of complementary numbers that we
 * have seen to form pairs. If the number is divisible by 60 - we have to look for complementary 0.
 * We should also recalculate the number of pairs before updating module count due to number
 * divisible by 30.
 */
import java.util.HashMap;
import java.util.Map;

class Solution {
  public int numPairsDivisibleBy60(int[] time) {
    Map<Integer, Integer> seenModulosCounts = new HashMap<>();
    int divisiblePairsCount = 0;
    for (int num : time) {
      int currentModulo = num % 60;
      int complementaryModulo = (60 - currentModulo) % 60;
      divisiblePairsCount += seenModulosCounts.getOrDefault(complementaryModulo, 0);
      seenModulosCounts.merge(currentModulo, 1, Integer::sum);
    }
    return divisiblePairsCount;
  }
}
