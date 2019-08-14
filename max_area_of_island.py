# -*- coding: utf-8 -*-
"""
Created on Tue Aug 13 20:43:54 2019

Leetcode: Max Area of Island

Given a non-empty 2D array grid of 0's and 1's, an island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

Find the maximum area of an island in the given 2D array. (If there is no island, the maximum area is 0.)

Example 1:

[[0,0,1,0,0,0,0,1,0,0,0,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,1,1,0,1,0,0,0,0,0,0,0,0],
 [0,1,0,0,1,1,0,0,1,0,1,0,0],
 [0,1,0,0,1,1,0,0,1,1,1,0,0],
 [0,0,0,0,0,0,0,0,0,0,1,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,0,0,0,0,0,0,1,1,0,0,0,0]]

Given the above grid, return 6. Note the answer is not 11, because the island must be connected 4-directionally. 


Time Complexity: O(m+n), iterate through entire graph once  
Space Complexity: O(1), keep track of constants 

@author: bohan
"""

class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        
        if not grid:
            return 0
        
        largest = 0
        def dfs(row, col, cnt):
            grid[row][col] = 0
            if row-1 >= 0 and grid[row-1][col] == 1:
                cnt = dfs(row-1, col, cnt+1)
            if col-1 >= 0 and grid[row][col-1] == 1:
                cnt = dfs(row,col-1, cnt+1)
            if row+1 < len(grid) and grid[row+1][col] == 1:
                cnt = dfs(row+1, col, cnt+1)
            if col+1<len(grid[0]) and grid[row][col+1] == 1:
                cnt = dfs(row, col+1, cnt+1)
            
            return cnt
            
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    largest = max(largest, dfs(i,j,1))
                
                
        return largest
                
                
                
                
                
                
        
        
        
        