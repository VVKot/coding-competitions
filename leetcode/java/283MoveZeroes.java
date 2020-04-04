/**
 * T: O(N) S: O(1)
 *
 * <p>Put a number from the original order to the new position when we encounter it. Always put a
 * zero in the current position in the case there is no more non-zero numbers in the array and it
 * should stay zero.
 */
class Solution {
  public void moveZeroes(int[] nums) {
    int writePointer = 0;
    for (int i = 0; i < nums.length; i++) {
      int currentNumber = nums[i];
      nums[i] = 0;
      if (currentNumber != 0) {
        nums[writePointer++] = currentNumber;
      }
    }
  }
}
