# -*- coding: utf-8 -*-
"""
Created on Sept 1, 2019
Leetcode: Diagonal Traverse

Given a matrix of M x N elements (M rows, N columns), return all elements of the matrix in diagonal order as shown in the below image.

Example:

Input:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]

Output:  [1,2,4,7,5,3,6,8,9]

Note:

The total number of elements of the given matrix will not exceed 10,000.

Time Complexity: O(m*n), traverse through matrix once
Space Complexity: O(m*n), size of output is size of matrix 

@author: bohan

"""


class Solution:
    def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:

        if not matrix:
            return None
        
        toRet = [matrix[0][0]]
        m = len(matrix)-1
        n = len(matrix[0])-1

        i= 0
        j = 0
        up = True

        while i != m or j != n:
            if up:
                while i-1 >= 0 and j+1<=n:
                    i -= 1
                    j += 1
                    toRet.append(matrix[i][j])
                
                if j + 1 <= n:
                    j += 1
                    toRet.append(matrix[i][j])
                    up = False
                elif i + 1 <= m:
                    i += 1
                    toRet.append(matrix[i][j])
                    up = False
            else:
                while i+1 <= m and j-1>=0:
                    i += 1
                    j -= 1
                    toRet.append(matrix[i][j])
                
                if i + 1 <= m:
                    i += 1
                    toRet.append(matrix[i][j])
                    up = True
                elif j + 1 <= n:
                    j += 1
                    toRet.append(matrix[i][j])
                    up = True
        
        return toRet

