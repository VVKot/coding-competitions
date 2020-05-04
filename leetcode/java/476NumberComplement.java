/**
 * T: O(1) S: O(1)
 *
 * <p>We go through each bit of the number, flip it, and assign the flipped bit to the new number.
 * To add the flipped bit in the correct place we need to remember the number of the current bit(its
 * shift).
 */
class Solution {
  public int findComplement(int num) {
    int result = 0;
    int shift = 0;
    while (num > 0) {
      int lastBit = num & 1;
      result |= (lastBit ^ 1) << shift;
      shift += 1;
      num >>= 1;
    }
    return result;
  }
}
