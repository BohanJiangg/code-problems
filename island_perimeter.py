# -*- coding: utf-8 -*-
"""
Created on August 13 2019  
Leetcode: Island Perimeter

You are given a map in form of a two-dimensional integer grid where 1 represents land and 0 represents water.

Grid cells are connected horizontally/vertically (not diagonally). The grid is completely surrounded by water, and there is exactly one island (i.e., one or more connected land cells).

The island doesn't have "lakes" (water inside that isn't connected to the water around the island). One cell is a square with side length 1. The grid is rectangular, width and height don't exceed 100. Determine the perimeter of the island.

Example:

Input:
[[0,1,0,0],
 [1,1,1,0],
 [0,1,0,0],
 [1,1,0,0]]

Output: 16

Time Complexity O(n), iterate through matrix once
Space Complexity: O(1), just need to keep track of counter
@author: bohan
"""

class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid:
            return 0

        peri = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    if i - 1 < 0 or grid[i-1][j] == 0:
                        peri+=1
                    if i + 1 >= len(grid) or grid[i+1][j] == 0:
                        peri+=1
                    if  j - 1 < 0 or grid[i][j-1] == 0:
                        peri += 1
                    if j + 1 >= len(grid[0]) or grid[i][j+1] == 0:
                        peri += 1
        return peri
