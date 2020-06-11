/**
 * T: O(N) S: O(1)
 *
 * <p>A solution without swapping which utilizes a fact that this problem does not require to swap
 * object by their key, just numbers. In that case, we can count the last position of zeroes and
 * ones, and insert the numbers at appropriate positions. We insert two by default so we don't need
 * a counter for it.
 */
class Solution {
  public void sortColors(int[] nums) {
    int numOfZeroes = 0;
    int numOfOnes = 0;
    for (int i = 0; i < nums.length; i++) {
      int num = nums[i];
      nums[i] = 2;
      if (num < 2) {
        nums[numOfOnes] = 1;
        numOfOnes++;
      }
      if (num == 0) {
        nums[numOfZeroes] = 0;
        numOfZeroes++;
      }
    }
  }
}
