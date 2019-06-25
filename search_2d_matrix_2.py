# -*- coding: utf-8 -*-
"""
Created on Sat Jun 15 14:22:02 2019

Leetcode: Search a 2D Matrix II

Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:
    Integers in each row are sorted in ascending from left to right.
    Integers in each column are sorted in ascending from top to bottom.


Time Complexity: O(m+n), for m columns and n rows
Space Complexity: O(1), only colIdx needed.   

@author: bohan

"""

class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        
        if not matrix:
            return False
        if not matrix[0]:
            return False
        
        # Comb matrix from right side to left
        colIdx = -1
        for row in matrix:
            while len(row) + colIdx >= 0 and row[len(row) + colIdx] > target:
                colIdx -= 1
            
            if row[len(row)+colIdx] == target:
                return True
        
        return False
            
        

#        DFS that takes too long        
#        isMarked = {}
#        stack = []
#        
#        if not matrix:
#            return False
#        if not matrix[0]:
#            return False
#        
#        rows = len(matrix)
#        cols = len(matrix[0])
#        
#        if matrix[0][0] > target:
#            return False
#        elif matrix[0][0] == target:
#            return True
#        
#        stack.append((0,0))
#        
#        while stack:
#            currIdx = stack.pop()
#            currVal = matrix[currIdx[0]][currIdx[1]]
#            
#            if not currVal in isMarked:
#                isMarked[currIdx] = True
#                
#                
#                if currIdx[0]+1 < rows and currIdx[1]+1 < cols:
#                    rightNum = matrix[currIdx[0]+1][currIdx[1]]
#                    downNum = matrix[currIdx[0]][currIdx[1]+1]
#                    diagNum = matrix[currIdx[0]+1][currIdx[1]+1]
#                    if rightNum == target or downNum == target or diagNum == target:
#                        return True
#                    else:
#                        nextList = []
#                        if rightNum < target:
#                            diff = target - rightNum
#                            nextList.append((currIdx[0]+1, currIdx[1], diff))
#                
#                        if downNum < target:
#                            diff = target - downNum
#                            if not nextList:
#                                nextList.append((currIdx[0], currIdx[1]+1, diff))
#                            elif diff > nextList[0][2]:
#                                nextList.append((currIdx[0], currIdx[1]+1, diff))
#                            else:
#                                nextList.insert(0, (currIdx[0], currIdx[1]+1, diff))
#                                
#                        if diagNum < target:
#                            diff = target - diagNum
#                            
#                            if not nextList:
#                                nextList.append((currIdx[0]+1, currIdx[1]+1, diff))
#                            else:
#                                i = 0
#                                while nextList[i][2] < diff:
#                                    i+=1
#                                nextList.insert(i, (currIdx[0]+1, currIdx[1]+1, diff))
#                        
#                        for item in nextList:
#                            stack.append((item[0], item[1]))
#                        
#
#                    
#                elif currIdx[0]+1 < rows:
#                    if matrix[currIdx[0]+1][currIdx[1]] == target:
#                        return True
#                    elif matrix[currIdx[0]+1][currIdx[1]] < target:
#                        stack.append((currIdx[0]+1, currIdx[1]))
#                elif currIdx[1]+1 < cols:
#                    if matrix[currIdx[0]][currIdx[1]+1] == target:
#                        return True
#                    elif matrix[currIdx[0]][currIdx[1]+1] < target:
#                        stack.append((currIdx[0], currIdx[1]+1))
#              
#        
#        return False
        
        