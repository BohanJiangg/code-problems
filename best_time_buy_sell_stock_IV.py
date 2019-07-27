# -*- coding: utf-8 -*-
"""
Created on Sat Jul 27 11:58:45 2019
Leetcode: Best Time to Buy and Sell Stock IV

Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete at most k transactions.

Note:
You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).

Example 1:

Input: [2,4,1], k = 2
Output: 2
Explanation: Buy on day 1 (price = 2) and sell on day 2 (price = 4), profit = 4-2 = 2.



Time Complexity: O(n),
Space Complexity: O(n),  

@author: bohan

"""

class Solution(object):
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        if not k or not prices:
            return 0
        
#        # Works, but Exceeds Memory Limit
#        buyTimes = [float('inf')] * k
#        profits = [0] *k
#        
#        for price in prices:
#            for i in range(k):
#                if i == 0:
#                    buyTimes[i] = min(buyTimes[i], price)
#                else:
#                    buyTimes[i] = min(buyTimes[i], price-profits[i-1])
#                profits[i] = max(profits[i], price-buyTimes[i])
#        
#        return profits[-1]
            
            
            
            
            
            
            
            