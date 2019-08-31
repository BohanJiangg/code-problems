# -*- coding: utf-8 -*-
"""
Created on August 31 2019
Leetcode: 01 Matrix

Given a matrix consists of 0 and 1, find the distance of the nearest 0 for each cell.

The distance between two adjacent cells is 1.

Example 1:

Input:
[[0,0,0],
 [0,1,0],
 [0,0,0]]

Output:
[[0,0,0],
 [0,1,0],
 [0,0,0]]

Note:

    The number of elements of the given matrix will not exceed 10,000.
    There are at least one 0 in the given matrix.
    The cells are adjacent in only four directions: up, down, left and right.

[[0,1,0,1,1],
 [1,1,0,0,1],
 [0,0,0,1,0],
 [1,0,1,1,1],
 [1,0,0,0,1]]

Time Complexity: O(n*m), go through matrix twice 
Space Complexity: O(1), modify matrix in place 

@author: bohan

"""

class Solution:
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        
        n = len(matrix)
        m = len(matrix[0])

        for i in range(n-1, -1, -1):
            for j in range(m-1, -1, -1):
                if matrix[i][j] != 0:
                    right = matrix[i][j+1] if j+1 < m else float('inf') 
                    down = matrix[i+1][j] if i+1 < n else float('inf')
                    matrix[i][j] = 1 + min(right, down)
        
        for i in range(n):
            for j in range(m):
                if matrix[i][j] != 0:
                    left = matrix[i-1][j] if i-1 >= 0 else float('inf')
                    top = matrix[i][j-1] if j-1 >= 0 else float('inf')
                    matrix[i][j] = min(matrix[i][j], 1+ min(left, top))

        return matrix