/**
 * T: O(N) S: O(N)
 *
 * <p>Remember numbers we have seen so far alongside their indices. Return a sorted pair of indices
 * when we see a number that is complement to the previously seen one.
 */
import java.util.HashMap;
import java.util.Map;

class Solution {
  public int[] twoSum(int[] nums, int target) {
    Map<Integer, Integer> seenNumbers = new HashMap<>();
    for (int i = 0; i < nums.length; i++) {
      int complement = target - nums[i];
      if (seenNumbers.containsKey(complement)) {
        return new int[] {seenNumbers.get(complement), i};
      }
      seenNumbers.put(nums[i], i);
    }
    return new int[] {-1, -1};
  }
}
