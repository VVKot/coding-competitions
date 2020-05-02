/**
 * T: O(J + S) S: O(J + S)
 *
 * <p>We create a set of known jewels to quickly look up against them and iterate over stones to
 * find all jewels. In the end, we just return the number of seen jewels.
 */
import java.util.Set;
import java.util.stream.Collectors;

class Solution {
  public int numJewelsInStones(String J, String S) {
    Set<Character> jewels = J.chars().mapToObj(ch -> (char) ch).collect(Collectors.toSet());
    int jewelsCount = 0;
    for (char stone : S.toCharArray()) {
      if (jewels.contains(stone)) {
        jewelsCount += 1;
      }
    }
    return jewelsCount;
  }
}
