/**
 * T: O(1) S: O(1)
 *
 * <p>The number is a power of two if it has only one bit set.
 */
class Solution {
  public boolean isPowerOfTwo(int n) {
    if (n <= 0) {
      return false;
    }
    return (x & (x - 1)) == 0;
  }
}
