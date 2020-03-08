class Solution(object):

    def maxProfit(self, prices):
        buy1, buy2 = float("-inf"), float("-inf")
        sell1, sell2 = 0, 0
        for price in prices:
            sell2 = max(sell2, buy2+price)
            buy2 = max(buy2, sell1-price)
            sell1 = max(sell1, buy1+price)
            buy1 = max(buy1, -price)
        return sell2
