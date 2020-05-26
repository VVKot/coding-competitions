/**
 * T: O(N) S: O(N)
 *
 * <p>We traverse through the array and remember the balance at the current position. If we have
 * seen such a balance already - there is a contiguous subarray that starts right after previous
 * occurence and ends at the current position. To handle zero balance we store an imaginary zero
 * balance at index -1.
 */
import java.util.HashMap;
import java.util.Map;

class Solution {
  public int findMaxLength(int[] nums) {
    Map<Integer, Integer> seenBalances = new HashMap<>();
    seenBalances.put(0, -1);
    int currentBalance = 0;
    int maxBalancedLength = 0;
    for (int i = 0; i < nums.length; i++) {
      int num = nums[i];
      currentBalance += num == 1 ? 1 : -1;
      if (seenBalances.containsKey(currentBalance)) {
        int previouslySeenPosition = seenBalances.get(currentBalance);
        maxBalancedLength = Math.max(maxBalancedLength, i - previouslySeenPosition);
      } else {
        seenBalances.put(currentBalance, i);
      }
    }
    return maxBalancedLength;
  }
}
