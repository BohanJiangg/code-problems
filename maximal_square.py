# -*- coding: utf-8 -*-
"""
Created on August 15 2019    
Leetcode: Maximal Square

Given a 2D binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.

Example:

Input: 

1 0 1 0 0
1 0 1 1 1
1 1 1 1 1
1 0 1 1 1

1 1 2 2 2
1 1 2 3 4
1 2 3 4 5
1 1 2 3 4

Output: 4


Time Complexity O(n), 
Space Complexity: O(1), 
@author: bohan
"""


class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        