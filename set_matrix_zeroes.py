# -*- coding: utf-8 -*-
"""
Created on Sat Oct 27 08:50:18 2018
Leetcode: Set Matrix Zeroes

Time Complexity: O(m x n) 
Space Complexity: O(m x n)

@author: bohan
"""

class Solution:
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        
        numRows = len(matrix)
        numCols = len(matrix[0])
        
        toZeroList = []

        
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if matrix[row][col] == 0:
                    toZeroList.append([row,col])

        
        for coord in toZeroList:
            coordRow = coord[0]
            coordCol = coord[1]
            for row in range(len(matrix)):
                matrix[row][coordCol] = 0
            for col in range(len(matrix[0])):
                matrix[coordRow][col] = 0
