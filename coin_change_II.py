# -*- coding: utf-8 -*-
"""
Created on Sun Jun 30 12:15:18 2019

CTCI: Problem 8.11 - Coins
Leetcode: Coin Change 2

You are given coins of different denominations and a total amount of money. Write a function to compute the number of combinations that make up that amount. You may assume that you have infinite number of each kind of coin.

Time Complexity: O()
Space Complexity: O(), 

@author: bohan

"""

class Solution(object):
    def change(self, amount, coins):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        """
        
        wip = [amount]
        result = 0 
        
        while wip:
            temp = []
            print(wip)
            for currSum in wip:
                for coin in coins:
                    if currSum - coin == 0 :
                        result += 1
                    elif currSum - coin > 0:
                        temp.append(currSum - coin)
            wip = list(dict.fromkeys(temp) ) 
        
        return result 