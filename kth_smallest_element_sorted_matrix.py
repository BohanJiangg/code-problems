# -*- coding: utf-8 -*-
"""
Created on July 18 2019
Leetcode: Kth Smallest Element in a Sorted Matrix

Given a n x n matrix where each of the rows and columns are sorted in ascending order, find the kth smallest element in the matrix.

Note that it is the kth smallest element in the sorted order, not the kth distinct element.

Example:

matrix = [
   [ 1,  5,  9],
   [10, 11, 13],
   [12, 13, 15]
],
k = 8,
return 13.

Note: 
You may assume k is always valid, 1 ≤ k ≤ n2.

Time Complexity O(n^2 log n^2), time required to sorted entire matrix 
Space Complexity: O(n^2), need to copy matrix into list 
@author: bohan
"""

class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        
        lis = []
        for row in matrix:
            lis += row
        
        lis = sorted(lis)

        return lis[k-1]












        
        




                    
        







