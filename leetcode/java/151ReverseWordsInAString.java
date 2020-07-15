import java.util.Arrays;
import java.util.Collections;
import java.util.List;

class Solution {
  public String reverseWords(String s) {
    s = s.trim();
    List<String> wordList = Arrays.asList(s.split("\\s+"));
    Collections.reverse(wordList);
    return String.join(" ", wordList);
  }
}
