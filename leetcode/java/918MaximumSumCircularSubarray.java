import java.util.Arrays;

class Solution {
  public int maxSubarraySumCircular(int[] A) {
    if (A.length == 1) {
        return A[0];
    }
    int arraySum = Arrays.stream(A).sum();
    int nonCircularMaxSum = Integer.MIN_VALUE;
    int current = Integer.MIN_VALUE;
    for (int num : A) {
      current = num + Math.max(current, 0);
      nonCircularMaxSum = Math.max(nonCircularMaxSum, current);
    }

    int startInteriorMaxSum = Integer.MAX_VALUE;
    current = Integer.MAX_VALUE;
    for (int i = 0; i < A.length - 1; i++) {
      current = A[i] + Math.min(current, 0);
      startInteriorMaxSum = Math.min(startInteriorMaxSum, current);
    }

    int endInteriorMaxSum = Integer.MAX_VALUE;
    current = Integer.MAX_VALUE;
    for (int i = 1; i < A.length; i++) {
      current = A[i] + Math.min(current, 0);
      endInteriorMaxSum = Math.min(endInteriorMaxSum, current);
    }
    endInteriorMaxSum = arraySum - endInteriorMaxSum;

    return Math.max(nonCircularMaxSum, Math.max(startInteriorMaxSum, endInteriorMaxSum));
  }
}
