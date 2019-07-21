# -*- coding: utf-8 -*-
"""
Created on Thu Jul  4 20:10:56 2019

Leetcode: Number of Islands

Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. 
An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. 
You may assume all four edges of the grid are all surrounded by water.


Time Complexity: O(n*m), where n*m is size of grid, worst case where everything is '1' dfs checks all nodes twice. 
Space Complexity: O(1), need to keep track of # islands only

@author: bohan

"""

class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid:
            return 0
        rows = len(grid)
        cols = len(grid[0])
        
        
        def dfs(row, col):
            
            if grid[row][col] == '0':
                return
            
            grid[row][col] = '0'
            
            if col + 1 < cols:
                dfs(row, col+1)
            if col - 1 >= 0:
                dfs(row, col-1)
            if row + 1 < rows:
                dfs(row+1, col)
            if row - 1 >= 0:
                dfs(row-1, col)
            
            return 
                
            
        
        islands = 0
        
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == '1':
                    islands += 1
                    dfs(row, col)
        
        
        return islands
        
                
            
            
            
            
            
            