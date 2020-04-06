/**
 * T: O(N) S: O(N)
 *
 * <p>Given that lengths of the elements are low, we can sort them to get a common representation
 * for an anagram. After that, all of anagrams will map to the same representation - collect them
 * and return at the end.
 */
import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

class Solution {
  public List<List<String>> groupAnagrams(String[] strs) {
    Map<String, List<String>> groups = new HashMap<>();
    for (String str : strs) {
      char[] chars = str.toCharArray();
      Arrays.sort(chars);
      String key = new String(chars);
      if (!groups.containsKey(key)) {
        groups.put(key, new ArrayList<String>());
      }
      List<String> existingValues = groups.get(key);
      existingValues.add(str);
      groups.put(key, existingValues);
    }
    return new ArrayList<List<String>>(groups.values());
  }
}
