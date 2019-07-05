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
        q = [(0,0)]
        isVisited = [(0,0)]
        numIslands = 0
        
        if grid[0][0] == "1":
            boundaries = {(0,1):'', (1,0):''}
        else:
            boundaries = {}
        
        while q:
            curr = q.pop(0)
            
            if curr in boundaries:
                del boundaries[curr]
                if not boundaries:
                    numIslands +=1
                    
            adjRight = None
            adjDown = None
            if (curr[0]+1 < len(grid) and curr[1] < len(grid[0])):
                adjDown = (curr[0]+1, curr[1])
            if (curr[0]< len(grid) and curr[1]+1 < len(grid[0])):
                adjRight = (curr[0], curr[1]+1)
            rightApp = downApp = 0
            if adjRight and not adjRight in isVisited:
                
                isVisited.append(adjRight)
                if grid[adjRight[0]][adjRight[1]] == "1":
                    boundaries[(adjRight[0]+1, adjRight[1])] = ''
                    boundaries[(adjRight[0], adjRight[1]+1)] = ''
                    rightApp = 1
                else:
                    rightApp = 2
            if adjDown and not adjDown in isVisited:
                
                isVisited.append(adjDown)
                if grid[adjDown[0]][adjDown[1]] == "1":
                    boundaries[(adjDown[0]+1, adjDown[1])] = ''
                    boundaries[(adjDown[0], adjDown[1]+1)] = ''
                    downApp = 2
                else:
                    downApp = 2
            
            if rightApp == 1 and downApp == 2:
                q.append(adjRight)
                q.append(adjDown)
            elif downApp == 1 and rightApp == 2:
                q.append(adjDown)
                q.append(adjRight)
            elif rightApp == 2 and downApp == 0:
                q.append(rightApp)
            elif downApp == 2 and rightApp == 0:
                q.append(downApp)
            elif rightApp == 2 and downApp ==2:
                q.append(adjDown)
                q.append(adjRight)
            
        
        return numIslands
            
            
            
            
            