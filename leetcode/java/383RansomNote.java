/**
 * T: O(R + M) S: O(M)
 *
 * <p>First, we count all available letters. After that, we iterate over the note and check if we
 * still have enough letters available, and return false otherwise. If we reach the end of the loop
 * - we can construct the note and return true.
 */
import java.util.HashMap;
import java.util.Map;

class Solution {
  public boolean canConstruct(String ransomNote, String magazine) {
    Map<Character, Integer> availableLetters = new HashMap<>();
    for (char ch : magazine.toCharArray()) {
      availableLetters.merge(ch, 1, Integer::sum);
    }
    for (char ch : ransomNote.toCharArray()) {
      if (!availableLetters.containsKey(ch)) {
        return false;
      }
      int availableLetterCount = availableLetters.get(ch);
      if (availableLetterCount <= 0) {
        return false;
      }
      availableLetters.put(ch, availableLetterCount - 1);
    }
    return true;
  }
}
