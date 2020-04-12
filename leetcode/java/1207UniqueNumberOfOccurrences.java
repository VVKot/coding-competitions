/**
 * T: O(N) S: O(N)
 *
 * <p>Count number of occurences of each elements. If all of those numbers are unique - return true,
 * otherwise - return false.
 */
import java.util.ArrayList;
import java.util.HashMap;
import java.util.HashSet;
import java.util.List;
import java.util.Map;

class Solution {
	public boolean uniqueOccurrences(int[] arr) {
		Map<Integer, Integer> numberCount = new HashMap<>();
		for (int number: arr) {
			numberCount.putIfAbsent(number, 0);
			numberCount.merge(number, 1, Integer::sum);
		}
		List<Integer> allNumberCounts = new ArrayList<>(numberCount.values());
		return allNumberCounts.size() == new HashSet<Integer>(allNumberCounts).size();
	}
}
