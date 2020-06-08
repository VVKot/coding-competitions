/**
 * T: O(logN) S: O(1)
 *
 * <p>The number is a power of two if it has only one bit set.
 */
class Solution {
  public boolean isPowerOfTwo(int n) {
    int setBitCount = 0;
    while (n > 0) {
      setBitCount += n & 1;
      n >>= 1;
    }
    return setBitCount == 1;
  }
}
