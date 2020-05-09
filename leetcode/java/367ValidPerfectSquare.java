/**
 * T: O(logN) S: O(1)
 *
 * <p>Use binary search to find the possible matching number, proceed until we either confirm that
 * there is a perfect root or we run out of candidates.
 */
class Solution {
  public boolean isPerfectSquare(int num) {
    if (num < 2) {
      return true;
    }
    long lo = 2;
    long hi = num / 2;
    while (lo <= hi) {
      long mid = lo + (hi - lo) / 2;
      long guessedSquare = mid * mid;
      if (guessedSquare == num) {
        return true;
      }
      if (guessedSquare > num) {
        hi = mid - 1;
      } else {
        lo = mid + 1;
      }
    }
    return false;
  }
}
