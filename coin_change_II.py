# -*- coding: utf-8 -*-
"""
Created on Sun Jun 30 12:15:18 2019

CTCI: Problem 8.11 - Coins
Leetcode: Coin Change 2

You are given coins of different denominations and a total amount of money. Write a function to compute the number of combinations that make up that amount. You may assume that you have infinite number of each kind of coin.

Time Complexity: O(n)
Space Complexity: O(n), where n is size of amount + 1 

@author: bohan

"""

class Solution(object):
    def change(self, amount, coins):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        """
        
        combinations = [0]*(amount+1)
        
        combinations[0] = 1
        
        for coin in coins:
            for idx in range(1, len(combinations)):
                if idx >= coin:
                    combinations[idx] += combinations[idx - coin]
                
        return combinations[amount]
        
        
        