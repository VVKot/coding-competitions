class Solution(object):
    def maxProfit(self, prices):
        if not prices:
            return 0
        max_profit = 0
        min_price = prices[0]
        max_price = prices[0]
        for i, price in enumerate(prices):
            # if price dropped or we reached the end of the period
            if price < max_price or i == len(prices) - 1:
                # call max to account for end of the period case
                max_profit += max(max_price, price) - min_price
                # we want to start over as history is no longer relevant at this point - we sold stock
                max_price = min_price = price
                continue
            min_price = min(min_price, price)
            max_price = max(max_price, price)
        return max_profit
