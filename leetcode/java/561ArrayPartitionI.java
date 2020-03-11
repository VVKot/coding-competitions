package leetcode.java;

/**
 * T: O(NlogN) S: O(1)
 *
 * We can determine the best solution greedily. We have to group numbers in sorted order and take
 * minimum of every pair which are at the odd positions.
 */
import java.util.Arrays;

class Solution {
  public int arrayPairSum(int[] nums) {
    Arrays.sort(nums);
    int result = 0;
    for (int i = 0; i < nums.length; i += 2) {
      result += nums[i];
    }
    return result;
  }
}
