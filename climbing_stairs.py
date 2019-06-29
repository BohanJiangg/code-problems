# -*- coding: utf-8 -*-
"""
Created on Sat Jun 29 14:23:28 2019

CTCI: Problem 8.1 - Triple Step
Leetcode: Climbing Stairs

You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Note: Given n will be a positive integer.

Time Complexity: O(n), one loop to go through every n
Space Complexity: O(1), only need to keep 3 constants.

@author: bohan

"""

class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1
        if n == 2:
            return 2
        
        a = 1
        b = 2
        c = a+b
        for i in range(2, n):
            c = a+b
            a = b
            b = c
        
        return c