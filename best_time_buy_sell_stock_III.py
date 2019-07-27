# -*- coding: utf-8 -*-
"""
Created on Sun Jul 21 11:49:39 2019
Leetcode: Best Time to Buy and Sell Stock III

Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete at most two transactions.

Note: You may not engage in multiple transactions at the same time (i.e., you must sell the stock before you buy again).


Input: [3,3,5,0,0,3,1,4]
Output: 6
Explanation: Buy on day 4 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.
             Then buy on day 7 (price = 1) and sell on day 8 (price = 4), profit = 4-1 = 3.


Time Complexity O(n), iterate through array once 
Space Complexity: O(1), need 4 pointers
@author: bohan
"""

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        buy1 = buy2 = float('inf')
        profit1 = profit2 = 0
        
        for price in prices:
            buy1 = min(buy1, price)
            profit1 = max(profit1, price-buy1)
            buy2 = min(buy2, price-profit1)
            profit2 = max(profit2, price-buy2)
        
        return profit2