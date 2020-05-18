/**
 * T: O(S) S: O(P)
 *
 * <p>First, we construct a counter of the P to find the exact counts of needed characters. After
 * that, we traverse the S one character at a time. If we find a needed character - we decrement the
 * missing counter, if we reach the length of the anagram and pop needed character from the left
 * side - we increment the missing counter. If this counter is 0 - we know that we have found an
 * anagram.
 */
import java.util.HashMap;
import java.util.LinkedList;
import java.util.List;
import java.util.Map;

class Solution {
  public List<Integer> findAnagrams(String s, String p) {
    Map<Character, Integer> anagramCharacters = new HashMap<>();
    for (char ch : p.toCharArray()) {
      anagramCharacters.merge(ch, 1, Integer::sum);
    }
    int anagramLength = p.length();
    int missingCharactersCount = anagramLength;
    List<Integer> anagramStartingPositions = new LinkedList<>();
    for (int i = 0; i < s.length(); i++) {
      char currentChar = s.charAt(i);
      if (anagramCharacters.containsKey(currentChar)) {
        int currentCharCount = anagramCharacters.get(currentChar);
        anagramCharacters.put(currentChar, currentCharCount - 1);
        if (currentCharCount >= 1) {
          missingCharactersCount -= 1;
        }
      }

      if (i >= anagramLength) {
        char charToPop = s.charAt(i - anagramLength);
        if (anagramCharacters.containsKey(charToPop)) {
          int charToPopCount = anagramCharacters.get(charToPop);
          anagramCharacters.put(charToPop, charToPopCount + 1);
          if (charToPopCount >= 0) {
            missingCharactersCount += 1;
          }
        }
      }

      if (missingCharactersCount == 0) {
        anagramStartingPositions.add(i - anagramLength + 1);
      }
    }
    return anagramStartingPositions;
  }
}
