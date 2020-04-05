/**
 * T: O(N) S: O(1)
 *
 * <p>The total profit is a sum of differences between the maximum and minimum values of the stock
 * price on zero or more intervals. If there are several increasing numbers between min and max on
 * some interval - sum of their differences it equal to the total differences. So, by finding
 * differences that increase profit we find total possible profit.
 */
class Solution {
  public int maxProfit(int[] prices) {
    int totalProfit = 0;
    for (int i = 1; i < prices.length; i++) {
      if (prices[i] > prices[i - 1]) {
        totalProfit += prices[i] - prices[i - 1];
      }
    }
    return totalProfit;
  }
}
