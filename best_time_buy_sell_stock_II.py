# -*- coding: utf-8 -*-
"""
Created on Sun Jun 30 16:12:12 2019

Leetcode: Best Time to Buy and Sell Stock II

Say you have an array for which the ith element is the price of a given stock on day i.
Design an algorithm to find the maximum profit. You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times).
Note: You may not engage in multiple transactions at the same time (i.e., you must sell the stock before you buy again).

Time Complexity: O(n), pass through prices once
Space Complexity: O(1), only need 1 constant  

@author: bohan

"""

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        
        maxProfit = 0
        
        for i in range(len(prices) - 1, 0, -1):
            if prices[i] > prices[i-1]:
                maxProfit += (prices[i] - prices[i-1])
        
        return maxProfit