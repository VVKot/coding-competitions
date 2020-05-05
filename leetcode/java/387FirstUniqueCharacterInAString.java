/**
 * T: O(N) S: O(N)
 *
 * <p>We iterate throught the string and keep track of the all seen characters. Whenever we see new
 * character - we add both to seen list and as a potential result. If we see a character for a
 * second time or more - we remove it from potential results list.
 */
import java.util.HashSet;
import java.util.LinkedHashMap;
import java.util.Map;
import java.util.Set;

class Solution {
  public int firstUniqChar(String s) {
    Map<Character, Integer> uniqueChars = new LinkedHashMap<>();
    Set<Character> seenChars = new HashSet<>();
    for (int i = 0; i < s.length(); i++) {
      char ch = s.charAt(i);
      if (seenChars.contains(ch)) {
        uniqueChars.remove(ch);
      } else {
        seenChars.add(ch);
        uniqueChars.put(ch, i);
      }
    }
    return uniqueChars.values().stream().findFirst().orElse(-1);
  }
}
