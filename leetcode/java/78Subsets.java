import java.util.ArrayList;
import java.util.List;

class Solution {
  private List<List<Integer>> result;
  private int[] numbers;

  public List<List<Integer>> subsets(int[] nums) {
    result = new ArrayList<>();
    numbers = nums;
    backtrack(new ArrayList<>(), 0);
    return result;
  }

  private void backtrack(List<Integer> subset, int index) {
    result.add(subset);
    for (int i = index; i < numbers.length; i++) {
      List<Integer> newSubset = new ArrayList<>(subset);
      newSubset.add(numbers[i]);
      backtrack(newSubset, i + 1);
    }
  }
}
