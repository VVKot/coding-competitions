import java.util.HashMap;
import java.util.Map;

class Solution {
  public int singleNumber(int[] nums) {
    Map<Integer, Integer> numsCount = new HashMap<>();
    for (int num : nums) {
      numsCount.put(num, numsCount.getOrDefault(num, 0) + 1);
    }

    for (int num : numsCount.keySet()) {
      if (numsCount.get(num) == 1) {
        return num;
      }
    }
    return -1;
  }
}
