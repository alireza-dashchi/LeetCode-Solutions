class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        total_profit = 0  # Start with no profit

        # Iterate through the array starting from the second day
        for i in range(1, len(prices)):
            # If today's price is higher than yesterday's, add the profit
            if prices[i] > prices[i - 1]:
                total_profit += prices[i] - prices[i - 1]

        return total_profit
