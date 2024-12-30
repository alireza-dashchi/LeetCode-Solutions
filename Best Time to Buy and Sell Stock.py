class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # Initialize variables
        buy_value = float('inf')  # Start with a very high value
        max_profit = 0  # Start with zero profit

        for price in prices:
            # Update the minimum price (buy_value)
            if price < buy_value:
                buy_value = price
            # Calculate profit if sold at the current price and update max_profit
            elif price - buy_value > max_profit:
                max_profit = price - buy_value

        return max_profit