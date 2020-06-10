/**
 * T: O(logN) S: O(1)
 *
 * <p>Peform a binary search.
 */
class Solution {
  public int searchInsert(int[] nums, int target) {
    int lo = 0;
    int hi = nums.length - 1;
    while (lo <= hi) {
      int mid = lo + (hi - lo) / 2;
      int atMid = nums[mid];
      if (atMid == target) {
        return mid;
      }
      if (atMid > target) {
        hi = mid - 1;
      } else {
        lo = mid + 1;
      }
    }
    return lo;
  }
}
