/**
 * T: O(logN) S: O(1)
 *
 * <p>Binary search through the array, check if the next element is the same as the current one. If
 * so - this means that the single element is further into array, if not - it is either current
 * element or some of the elements before. We only need to check the even indexes to avoid redundant
 * computation.
 */
class Solution {
  public int singleNonDuplicate(int[] nums) {
    int lo = 0;
    int hi = nums.length - 1;
    while (lo < hi) {
      int mid = lo + (hi - lo) / 2;
      if (mid % 2 == 1) {
        mid--;
      }
      if (nums[mid] == nums[mid + 1]) {
        lo = mid + 2;
      } else {
        hi = mid;
      }
    }
    return nums[lo];
  }
}
