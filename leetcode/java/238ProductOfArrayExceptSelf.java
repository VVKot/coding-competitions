/**
 * T: O(N) S: O(1)
 *
 * <p>To not use any intermediate space we remember the last seen multiplier and multiply every
 * element by it. Multiplication should be done before changing the multiplier to satisfy "except
 * self" requirement.
 */
import java.util.Arrays;

class Solution {
  public int[] productExceptSelf(int[] nums) {
    int[] multipliedNums = new int[nums.length];
    Arrays.fill(multipliedNums, 1);
    int multiplier = 1;
    for (int i = 0; i < nums.length; i++) {
      multipliedNums[i] *= multiplier;
      multiplier *= nums[i];
    }
    multiplier = 1;
    for (int i = nums.length - 1; i >= 0; i--) {
      multipliedNums[i] *= multiplier;
      multiplier *= nums[i];
    }
    return multipliedNums;
  }
}
