# -*- coding: utf-8 -*-
"""
Created on Thu Jul 25 19:43:09 2019
Leetcode: Fibonacci Number

The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, such that each number is the sum of the two preceding ones, starting from 0 and 1. That is,

F(0) = 0,   F(1) = 1
F(N) = F(N - 1) + F(N - 2), for N > 1.

Given N, calculate F(N).

Example 1:

Input: 2
Output: 1
Explanation: F(2) = F(1) + F(0) = 1 + 0 = 1.

Time Complexity: O(N), need to calculated fib for N from 0 to N
Space Complexity: O(N), need to memoize the fib number for each N  

@author: bohan

"""

class Solution(object):
    def fib(self, N):
        """
        :type N: int
        :rtype: int
        """
        if N == 0:
            return 0
        if N == 1:
            return 1
        
        dp = [0,1]+[None]*(N-1)
        
        def recursiveFunc(curr):
            if dp[curr] != None:
                return dp[curr]
            else:
                dp[curr] = recursiveFunc(curr-1) + recursiveFunc(curr-2)
                return dp[curr]
                
                
        return recursiveFunc(N)
        
        
        