/**
 * T: O(A * N) S: O(N)
 *
 * <p>For each coin C, we can make amount A exactly the same number of times as we can make A-C.
 * Applying the same logic from the bottom up for each coin we get the final solution. The only
 * trick is to account for zero - we can reach in just one way by not picking any coins.
 */
class Solution {
  public int change(int amount, int[] coins) {
    int[] dp = new int[amount + 1];
    dp[0] = 1;

    for (int coin : coins) {
      for (int i = coin; i < amount + 1; i++) {
        dp[i] += dp[i - coin];
      }
    }
    return dp[amount];
  }
}
