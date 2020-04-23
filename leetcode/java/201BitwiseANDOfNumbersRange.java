/**
 * T: O(1) S: O(1)
 *
 * <p>One observation to make is that result if always the common prefix between all numbers. After
 * that, at least one of the number will have a zero in the corresponding bit hence this bit in
 * result will be zero. To find the biggest common prefix we continuously right shift both end of
 * the range until they are the same.
 */
class Solution {
  public int rangeBitwiseAnd(int m, int n) {
    int shift = 0;
    while (m != n) {
      shift += 1;
      m >>= 1;
      n >>= 1;
    }
    return n << shift;
  }
}
