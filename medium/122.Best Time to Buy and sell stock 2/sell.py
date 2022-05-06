class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # i = 0
        # profit = 0
        # while i + 1 < len(prices):
        #     if prices[i] < prices[i+1]:
        #         profit += prices[i+1] - prices[i]
        #     i+=1
        # return profit
        profit = 0
        for i in range(1, len(prices)):
            if prices[i-1] < prices[i]:
                profit += prices[i] - prices[i-1] 
        return profit

