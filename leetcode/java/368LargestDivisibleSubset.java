import java.util.ArrayList;
import java.util.Arrays;
import java.util.LinkedList;
import java.util.List;

class Solution {
  public List<Integer> largestDivisibleSubset(int[] nums) {
    int N = nums.length;
    if (N == 0) return new ArrayList<>();

    Integer[] dp = new Integer[N];

    Arrays.sort(nums);

    int maxSubsetSize = -1;
    int maxSubsetIndex = -1;

    for (int i = 0; i < N; ++i) {
      int subsetSize = 0;

      for (int k = 0; k < i; ++k) {
        if (nums[i] % nums[k] == 0 && subsetSize < dp[k]) subsetSize = dp[k];
      }

      dp[i] = subsetSize + 1;

      if (maxSubsetSize < dp[i]) {
        maxSubsetSize = dp[i];
        maxSubsetIndex = i;
      }
    }

    LinkedList<Integer> largestSubset = new LinkedList<>();
    int currSize = maxSubsetSize;
    int currTail = nums[maxSubsetIndex];
    for (int i = maxSubsetIndex; i >= 0; --i) {
      if (currSize == 0) {
        break;
      }

      if (currTail % nums[i] == 0 && currSize == dp[i]) {
        largestSubset.addFirst(nums[i]);
        currTail = nums[i];
        currSize -= 1;
      }
    }

    return largestSubset;
  }
}
