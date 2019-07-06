# -*- coding: utf-8 -*-
"""
Created on Thu Jul  4 20:10:56 2019

Leetcode: Number of Islands

Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Time Complexity: O(n), 
Space Complexity: O(1),

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
        
        isVisited = []
        
        q = [(0,0)]
        numIslands = 0
        while q:
            row,col = q.pop(0)
            
            isVisited.append((row,col))
            
            if grid[row][col] == 1:
                
            
            
            
            
            
            