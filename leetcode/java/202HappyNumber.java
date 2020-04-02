/**
 * T: O(logN) S: O(logN)
 *
 * <p>Perform the computation described in the program, remember seen numbers. If we detect a loop -
 * the number is not happy. Otherwise, the number will end up at 1.
 */
import java.util.HashSet;
import java.util.Set;

class Solution {
  public boolean isHappy(int n) {
    Set<Integer> seenNumbers = new HashSet<>();
    while (n != 1) {
      if (seenNumbers.contains(n)) {
        return false;
      }
      seenNumbers.add(n);
      int nextNum = 0;
      while (n != 0) {
        int currentDigit = n % 10;
        nextNum += currentDigit * currentDigit;
        n /= 10;
      }
      n = nextNum;
    }
    return true;
  }
}
