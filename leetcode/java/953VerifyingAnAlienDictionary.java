/**
 * T: O(N) S: O(1)
 *
 * <p>Find the relative position of every character. Compare each two adjacent words - if the latter
 * one is bigger, the word sequence is not sorted.
 */
import java.util.HashMap;
import java.util.Map;

class Solution {
  public boolean isAlienSorted(String[] words, String order) {
    Map<Character, Integer> charPositions = getCharPositions(order);
    for (int j = 0; j < words.length - 1; j++) {
      if (!isWordSmaller(words[j], words[j + 1], charPositions)) {
        return false;
      }
    }
    return true;
  }

  private Map<Character, Integer> getCharPositions(String order) {
    Map<Character, Integer> charPositions = new HashMap<>();
    for (int i = 0; i < order.length(); i++) {
      charPositions.put(order.charAt(i), i);
    }
    return charPositions;
  }

  private boolean isWordSmaller(
      String string, String string2, Map<Character, Integer> charPositions) {
    for (int i = 0; i < string.length() && i < string2.length(); i++) {
      int position = charPositions.get(string.charAt(i));
      int position2 = charPositions.get(string2.charAt(i));
      if (position < position2) {
        return true;
      }
      if (position > position2) {
        return false;
      }
    }
    return string.length() < string2.length();
  }
}
