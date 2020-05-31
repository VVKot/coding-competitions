class Solution {
  public int minDistance(String word1, String word2) {
    int l1 = word1.length();
    int l2 = word2.length();
    int[] dp = new int[l2 + 1];
    for (int i = 0; i < l2 + 1; i++) {
      dp[i] = i;
    }
    for (int i = 1; i <= l1; i++) {
      int prev = i;
      for (int j = 1; j <= l2; j++) {
        int curr = 0;
        if (word1.charAt(i - 1) == word2.charAt(j - 1)) {
          curr = dp[j - 1];
        } else {
          int minPrev = Math.min(prev, dp[j - 1]);
          curr = Math.min(minPrev, dp[j]) + 1;
        }
        dp[j - 1] = prev;
        prev = curr;
      }
      dp[l2] = prev;
    }
    return dp[l2];
  }
}
