# DS: Array
# ALGO: Sliding Window
# Time: O(n). Space: O(1)

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        low = prices[0]
        max_profit = 0

        for p in prices:
            if p < low:
                low = p
            elif p > low:
                max_profit = max(max_profit, p - low)

        return max_profit
