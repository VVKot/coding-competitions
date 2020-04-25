/**
 * T: O(N) S: O(1)
 *
 * <p>Track the last reachable position for every iteration. If we can reach it from the current
 * index - we can still reach the end, so we mark current index as reachable. In the end, if we were
 * able to reach beginning of the array - the end is reachable.
 */
class Solution {
  public boolean canJump(int[] nums) {
    int lastReachablePosition = nums.length - 1;
    for (int i = nums.length - 1; i >= 0; i--) {
      if (i + nums[i] >= lastReachablePosition) {
        lastReachablePosition = i;
      }
    }
    return lastReachablePosition == 0;
  }
}
