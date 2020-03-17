/**
 * T: O(N) S: O(N)
 *
 * <p>Use stack to remember the last seen symbol. If it does not match with a new symbol - this is
 * not a valid sequence. If there are still unmatched symbols after the end of the loop - this is
 * not a valid sequence. Otherwise, it is a valid sequence.
 */
import java.util.Map;
import java.util.Stack;

class Solution {
  public boolean isValid(String s) {
    Stack<Character> seenCharacters = new Stack<>();
    Map<Character, Character> closedSymbolsToOpenMap =
        Map.of(
            ']', '[',
            ')', '(',
            '}', '{');
    for (char ch : s.toCharArray()) {
      if (closedSymbolsToOpenMap.containsKey(ch)) {
        if (seenCharacters.isEmpty()) {
          return false;
        }
        char lastSeenCh = seenCharacters.pop();
        if (lastSeenCh != closedSymbolsToOpenMap.get(ch)) {
          return false;
        }
      } else {
        seenCharacters.push(ch);
      }
    }
    return seenCharacters.isEmpty();
  }
}
