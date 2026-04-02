class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        for i in range(len(prices)):
            for j in range(i+1,len(prices)):
                current_profit = prices[j] - prices[i]
                profit = max(profit, current_profit)
        return profit