class Solution():
    def coinChange(self, coins, amount):
        max_ = float('inf')
        coin_count = [0] + [max_] * amount

        for i in range(1, amount + 1):
            coin_count[i] = min(
                [coin_count[i - c] if i - c >= 0 else max_ for c in coins]) + 1

        return -1 if coin_count[amount] == max_ else coin_count[amount]
