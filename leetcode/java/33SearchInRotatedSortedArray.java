/**
 * T: O(logN) S: O(1)
 *
 * <p>First, find the index of the smallest element. Now we can can find which part of the array
 * target belongs to and execute binary search.
 */
class Solution {
  private final int NUM_NOT_FOUND = -1;

  public int search(int[] nums, int target) {
    if (nums.length == 0) {
      return NUM_NOT_FOUND;
    }
    int minIndex = findMinIndex(nums);
    if (target >= nums[minIndex] && target <= nums[nums.length - 1]) {
      return binarySearch(nums, target, minIndex, nums.length - 1);
    }
    return binarySearch(nums, target, 0, minIndex - 1);
  }

  private int findMinIndex(int[] nums) {
    int left = 0;
    int right = nums.length - 1;
    while (left != right) {
      int mid = (left + right) / 2;
      if (nums[mid] > nums[right]) {
        left = mid + 1;
      } else {
        right = mid;
      }
    }
    return left;
  }

  private int binarySearch(int[] nums, int target, int left, int right) {
    while (left <= right) {
      int mid = (left + right) / 2;
      if (nums[mid] > target) {
        right = mid - 1;
      } else if (nums[mid] < target) {
        left = mid + 1;
      } else {
        return mid;
      }
    }
    return NUM_NOT_FOUND;
  }
}
