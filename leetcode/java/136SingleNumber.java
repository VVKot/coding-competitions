/**
 * T: O(N) S: O(1)
 *
 * <p>Reduce array using XOR. Since A ^ A = 0, pairs of numbers are eliminated and what's left is
 * the result.
 */
class Solution {
  public int singleNumber(int[] nums) {
    int result = 0;
    for (int num : nums) {
      result ^= num;
    }
    return result;
  }
}
