/**
 * T: O(S + SH) S: O(S)
 *
 * <p>Iterate over the whole string, find overall shift. Use modulo to not perform shift that is
 * larger than length of the array. Space complexity is still linear due to the need of creation of
 * a new string.
 */
class Solution {
  public String stringShift(String s, int[][] shift) {
    int totalShift = 0;
    for (int[] shiftOperation : shift) {
      int direction = shiftOperation[0];
      int amount = shiftOperation[1];
      totalShift += direction == 0 ? amount : -amount;
    }
    int stringLength = s.length();
    totalShift = (totalShift % stringLength + stringLength) % stringLength;
    return s.substring(totalShift) + s.substring(0, totalShift);
  }
}
