/**
 * T: O(N) S: O(N)
 *
 * <p>Track all seen prefix sums. If we have seen a prefix sum of total - K value then we have a
 * subarray of value K between the end of this prefix and current element. If we have seen such
 * prefix several times - we have to account for all occurences.
 */
import java.util.HashMap;
import java.util.Map;

class Solution {
  public int subarraySum(int[] nums, int k) {
    int subarrayCount = 0;
    int totalSum = 0;
    Map<Integer, Integer> seenPrefixSums = new HashMap<>();
    seenPrefixSums.put(0, 1);
    for (int num : nums) {
      totalSum += num;
      subarrayCount += seenPrefixSums.getOrDefault(totalSum - k, 0);
      seenPrefixSums.merge(totalSum, 1, Integer::sum);
    }
    return subarrayCount;
  }
}
