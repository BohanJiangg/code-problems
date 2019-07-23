# -*- coding: utf-8 -*-
"""
Created on Mon Jul 22 19:20:56 2019
Leetcode: Coin Change

You are given coins of different denominations and a total amount of money amount. Write a function to compute the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

Example 1:

Input: coins = [1, 2, 5], amount = 11
Output: 3 
Explanation: 11 = 5 + 5 + 1

Note:
You may assume that you have an infinite number of each kind of coin.

Time Complexity O(amount * len(coins)), iterate through coins for each number from 1 to amount 
Space Complexity: O(amount), need array to store amount
@author: bohan
"""

class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        
        if amount == 0:
            return 0
        
        MAX = float('inf')
        dp = [0] + [MAX] * amount
       
        for i in range(1, amount+1):
            dp[i] = min([dp[i-c] if i - c >= 0 else MAX for c in coins]) + 1
        
        
        if dp[amount] == MAX:
            return -1
        else:
            return dp[amount]
       
       
       
       
        
        
        