# -*- coding: utf-8 -*-
"""
Created on July 11 2019
Leetcode: Minimum Path Sum

Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.

Time Complexity O(n*m), iterate through matrix once 
Space Complexity: O(1), modify matrix entries in place. 
@author: bohan
"""

class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        rows = len(grid)
        cols = len(grid[0])

        for i in range(rows):
            for j in range(cols):
                if i == 0 and j > 0:
                    grid[i][j] = grid[i][j-1] + grid[i][j]
                elif j == 0 and i > 0:
                    grid[i][j] = grid[i-1][j] + grid[i][j]
                elif i > 0 and j > 0:
                    grid[i][j] = min(grid[i-1][j], grid[i][j-1]) + grid[i][j]
        
        return grid[rows-1][cols-1]



        

        # Below solution uses an extra matrix and is too slow
        # rows = len(grid)
        # cols = len(grid[0])

        # retGrid = []
        # for i in range(rows):
        #     retGrid.append([])
        #     for j in range(cols):
        #         retGrid[i].append(float('inf'))

        # retGrid[0][0] = grid[0][0]

        # q = [(0,0)]
        # visited = [(0,0)]
        # while q:
        #     currCoords = q.pop(0)
        #     currVal = grid[currCoords[0]][currCoords[1]]
        #     # check top and check left and get min
        #     if currCoords[1] - 1 >= 0:
        #         retGrid[currCoords[0]][currCoords[1]] = min((retGrid[currCoords[0]][currCoords[1]-1] + currVal), retGrid[currCoords[0]][currCoords[1]])

        #     if currCoords[0] - 1 >= 0:
        #         retGrid[currCoords[0]][currCoords[1]] = min((retGrid[currCoords[0]-1][currCoords[1]] + currVal), retGrid[currCoords[0]][currCoords[1]])

        #     # check for bottom and right and append
        #     if (currCoords[0] < rows) and (currCoords[1] + 1 < cols):
        #         if not (currCoords[0], currCoords[1]+1) in visited:
        #             q.append((currCoords[0], currCoords[1]+1))
        #             visited.append((currCoords[0], currCoords[1]+1))
            
        #     if currCoords[1] < cols and currCoords[0] + 1 < rows:
        #         if not (currCoords[0]+1, currCoords[1]) in visited:
        #             q.append((currCoords[0]+1, currCoords[1]))
        #             visited.append((currCoords[0]+1, currCoords[1]))

        # return retGrid[rows-1][cols-1] 