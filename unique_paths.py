# -*- coding: utf-8 -*-
"""
Created on Sat Jun 29 15:13:51 2019

CTCI: Problem 8.2 - Robot in a Grid (without off-limits)
Leetcode: Unique Paths

A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

How many possible unique paths are there?

Time Complexity: O(nm), go through the grid once
Space Complexity: O(m*n), need to store values for each value once  

@author: bohan
"""

class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        if m == 1 and n == 1:
            return 1
        if m == 1 or n == 1:
            return 1
        if m == 2 and n == 2:
            return 2
            
            
        memo = {}
        memo[(m,n)] = 0
        memo[(m-1,n)] = 1
        memo[(m,n-1)] = 1
        #m = m-1
        for currN in range(n, 0, -1):
            for currM in range(m, 0, -1):
                if (currM, currN) != (m,n) and (currM, currN) != (m-1, n) and (currM, currN) != (m, n-1):
                    if currN == n:
                        memo[(currM, currN)] = memo[(currM+1, currN)]
                    elif currM == m:
                        memo[(currM, currN)] = memo[(currM, currN+1)]
                    else:
                        memo[(currM, currN)] = memo[(currM+1, currN)] + memo[(currM, currN+1)]
        
        return memo[(1,1)]
        
        