# -*- coding: utf-8 -*-
"""
Created on Sun May 12 14:08:22 2019

CTCI: Problem 1.7 - Rotate Matrix
Leetcode: Rotate Image

You are given an n x n 2D matrix representing an image.

Rotate the image by 90 degrees (clockwise).

Note:
You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.


Time Complexity: O(n), iterate through all values in matrix
Space Complexity: O(1), in-place nested list iteration

@author: bohan
"""


class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        matrix[:] = [ [row[i] for row in matrix[::-1]] for i in range(len(matrix))]
        
        
        