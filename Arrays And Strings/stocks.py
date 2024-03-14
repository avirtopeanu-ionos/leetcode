"""
Input: 
    [7,1,5,3,6,4]
Output: 
    5
Explanation: 
    Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
    Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
"""

from typing import List
import math


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float('inf')
        max_profit = 0
        
        for price in prices:
            if price < min_price:
                # Buy if lowest price seen so far
                min_price = price
            elif price - min_price > max_profit:
                # Try selling and seeing if we get more money this time
                max_profit = price - min_price
                
        return max_profit


if __name__ == "__main__":
    print(Solution().maxProfit(
        [7, 1, 5, 3, 6, 4]
    ))