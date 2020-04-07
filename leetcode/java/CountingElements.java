import java.util.HashSet;
import java.util.Set;

class Solution {
  public int countElements(int[] arr) {
    Set<Integer> seenNums = new HashSet<>();
    for (int num : arr) {
      seenNums.add(num);
    }
    int numsCount = 0;
    for (int num : arr) {
      if (seenNums.contains(num + 1)) {
        numsCount++;
      }
    }
    return numsCount;
  }
}
