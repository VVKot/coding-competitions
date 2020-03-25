/**
 * T: O(N) S: O(N)
 *
 * <p>Count number of occurences of each elements. If all of those numbers are unique - return true,
 * otherwise - return false.
 */
import java.util.Collection;
import java.util.HashSet;
import java.util.Map;

class Solution {
  public boolean uniqueOccurences(int[] arr) {
    Map<int, int> numberCount = new HashMap<>();
    for (int number : arr) {
      numberCount.putIfAbsent(number, 0);
      numberCount.merge(number, 1, Integer::sum);
    }
    Collection<int> allNumberCounts = numberCount.values();
    return allNumberCounts.size() == new HashSet(allNumberCounts).size();
  }
}
