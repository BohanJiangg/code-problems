# -*- coding: utf-8 -*-
"""
Created on Sun Aug 11 11:46:47 2019

Leetcode: Range Sum Query 2D - Immutable

Given a 2D matrix matrix, find the sum of the elements inside the rectangle defined by its upper left corner (row1, col1) and lower right corner (row2, col2).

Range Sum Query 2D
The above rectangle (with the red border) is defined by (row1, col1) = (2, 1) and (row2, col2) = (4, 3), which contains sum = 8.

Example:

Given matrix = [
  [3, 0, 1, 4, 2],
  [5, 6, 3, 2, 1],
  [1, 2, 0, 1, 5],
  [4, 1, 0, 1, 7],
  [1, 0, 3, 0, 5]
]

sumRegion(2, 1, 4, 3) -> 8
sumRegion(1, 1, 2, 2) -> 11
sumRegion(1, 2, 2, 4) -> 12

Time Complexity: O(m*n), for prefix sums construction, then O(m) per query 
Space Complexity: O(m*n), need to make a prefix sums row for each row in matrix

@author: bohan
"""

class NumMatrix(object):

    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        if not matrix:
            self.row_sums = []
        else:
            self.row_sums = [[0] * len(matrix[0]) for i in range(len(matrix))]
            
            for i in range(len(matrix)):
                for j in range(len(matrix[0])):
                    if j == 0:
                        self.row_sums[i][j] = matrix[i][j]
                    else:
                        self.row_sums[i][j] = self.row_sums[i][j-1] + matrix[i][j]
        
    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        
        toRet = 0
        for i in range(row1, row2+1):
            if col1 == 0:
                toRet += self.row_sums[i][col2]
            else:
                toRet += self.row_sums[i][col2] - self.row_sums[i][col1-1]
        
        return toRet
        
        # Below solution works but too slow O(n^2)
        '''
        toRet = 0
        for i in range(row1, row2+1):
            for j in range(col1, col2+1):
                toRet += self.matrix[i][j]
        return toRet
        '''        
        
        
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)