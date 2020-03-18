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
      String currentWord, String nextWord, Map<Character, Integer> charPositions) {
    for (int i = 0; i < currentWord.length() && i < nextWord.length(); i++) {
      int currentWordCharPosition = charPositions.get(currentWord.charAt(i));
      int nextWordCharPosition = charPositions.get(nextWord.charAt(i));
      if (currentWordCharPosition < nextWordCharPosition) {
        return true;
      }
      if (currentWordCharPosition > nextWordCharPosition) {
        return false;
      }
    }
    return currentWord.length() < nextWord.length();
  }
}
