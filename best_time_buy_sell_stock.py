# -*- coding: utf-8 -*-
"""
Created on June 14 2019
Leetcode: Best Time to Buy and Sell Stock

Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock), design an algorithm to find the maximum profit.

Note that you cannot sell a stock before you buy one.

Example 1:

Input: [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
             Not 7-1 = 6, as selling price needs to be larger than buying price.

Time Complexity O(n), go through prices once to find max and second time to keep track of minimum while finding largest difference
Space Complexity: O(1), Only need minPrice, maxProfit as constants. 
@author: bohan
"""

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        minPrice = max(prices)
        maxProfit = 0
        for i in range(len(prices)):
            # if and elif here because if the minPrice is new, then only subsequent prices can be considered in the max profit
            # maxProfit not updated until after in case new minPrice doesn't result in a maxprofit result 
            if prices[i] < minPrice:
                minPrice = prices[i]
            elif prices[i] - minPrice > maxProfit:
                maxProfit = prices[i] - minPrice

        return maxProfit