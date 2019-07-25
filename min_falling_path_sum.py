# -*- coding: utf-8 -*-
"""
Created on July 25 2019
Leetcode: Minimum Falling Path Sum

Given a square array of integers A, we want the minimum sum of a falling path through A.

A falling path starts at any element in the first row, and chooses one element from each row.  The next row's choice must be in a column that is different from the previous row's column by at most one.

Example 1:

Input: [[1,2,3],[4,5,6],[7,8,9]]
Output: 12
Explanation: 
The possible falling paths are:
[1,4,7], [1,4,8], [1,5,7], [1,5,8], [1,5,9]
[2,4,7], [2,4,8], [2,5,7], [2,5,8], [2,5,9], [2,6,8], [2,6,9]
[3,5,7], [3,5,8], [3,5,9], [3,6,8], [3,6,9]
The falling path with the smallest sum is [1,4,7], so the answer is 12.

Time Complexity O(n^2), iterate through entire matrix
Space Complexity: O(1), done in-place
@author: bohan
"""

class Solution(object):
    def minFallingPathSum(self, A):
        """
        :type A: List[List[int]]
        :rtype: int
        """
        if not A:
            return 0
        length = len(A)
        for row in range(len(A)-2, -1, -1):
            for col in range(length):
                if col + 1 < length and col-1 >= 0:
                    A[row][col] += min(A[row+1][col], A[row+1][col-1], A[row+1][col+1])
                elif col-1 < 0:
                    A[row][col] += min(A[row+1][col], A[row+1][col+1])
                else: # col + 1 >= length
                    A[row][col] += min(A[row+1][col], A[row+1][col-1])
        
        return min(A[0])
                


                    




        
