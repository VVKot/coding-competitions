/**
 * T: O(NlogN) S: O(N)
 *
 * <p>Count all characters, sort them in descending order, append the appropriate amount of
 * characters to the result.
 */
import java.util.ArrayList;
import java.util.Collections;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

class Solution {
  public String frequencySort(String s) {
    Map<Character, Integer> charCounts = new HashMap<>();
    for (char ch : s.toCharArray()) {
      charCounts.put(ch, charCounts.getOrDefault(ch, 0) + 1);
    }
    List<Character> chars = new ArrayList<>(charCounts.keySet());
    Collections.sort(chars, (a, b) -> charCounts.get(b) - charCounts.get(a));
    StringBuilder result = new StringBuilder();
    for (char ch : chars) {
      int charCount = charCounts.get(ch);
      for (int i = 0; i < charCount; i++) {
        result.append(ch);
      }
    }
    return result.toString();
  }
}
