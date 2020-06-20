import java.util.ArrayList;
import java.util.List;

class Solution {
  public String getPermutation(int n, int k) {
    int[] factorials = new int[n];
    List<Integer> nums =
        new ArrayList<>() {
          {
            add(1);
          }
        };

    factorials[0] = 1;
    for (int i = 1; i < n; ++i) {
      factorials[i] = factorials[i - 1] * i;
      nums.add(i + 1);
    }

    --k;
    StringBuilder permutation = new StringBuilder();
    for (int i = n - 1; i > -1; --i) {
      int index = k / factorials[i];
      k -= index * factorials[i];

      permutation.append(nums.get(index));
      nums.remove(index);
    }
    return permutation.toString();
  }
}
