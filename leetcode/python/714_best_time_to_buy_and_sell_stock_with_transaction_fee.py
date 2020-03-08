class Solution:
    def maxProfit(self, prices, fee):
        N = len(prices)
        if N < 2:
            return 0
        ans = 0
        minimum = prices[0]
        for i in range(1, N):
            if prices[i] < minimum:
                minimum = prices[i]
            elif prices[i] > minimum + fee:
                ans += prices[i] - fee - minimum
                minimum = prices[i] - fee
        return ans
