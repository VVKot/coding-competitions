/**
 * T: O(NlogN) S: O(N)
 *
 * <p>Use TreeMap to count elements and sort them by the key at the same time. Fill the beginning of
 * the array with the numbers from arr2 that were present in arr1, add the rest of the arr1 to the
 * end.
 */
import java.util.TreeMap;

class Solution {
  public int[] relativeSortArray(int[] arr1, int[] arr2) {
    TreeMap<Integer, Integer> elementsCount = new TreeMap<>();
    for (int num : arr1) {
      elementsCount.merge(num, 1, Integer::sum);
    }
    int writeIndex = 0;
    for (int num : arr2) {
      for (int i = 0; i < elementsCount.get(num); i++) {
        arr1[writeIndex++] = num;
      }
      elementsCount.remove(num);
    }
    for (int num : elementsCount.keySet()) {
      for (int i = 0; i < elementsCount.get(num); i++) {
        arr1[writeIndex++] = num;
      }
    }
    return arr1;
  }
}
