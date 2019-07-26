# -*- coding: utf-8 -*-
"""
Created on July 26, 2019
Leetcode: Triangle

Given a triangle, find the minimum path sum from top to bottom. Each step you may move to adjacent numbers on the row below.

For example, given the following triangle

[
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
The minimum path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1 = 11).

Note:

Bonus point if you are able to do this using only O(n) extra space, where n is the total number of rows in the triangle.

Time Complexity: O(n), iterate through triangle once
Space Complexity: O(1), modify the triangle in-place

@author: bohan
"""

class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """

        # Go from n - 1 row and work way up

        if not triangle:
            return None
        if len(triangle) == 1:
            return triangle[0][0]
        

        for row in range(len(triangle)-2, -1, -1):
            for num in range(len(triangle[row])):
                triangle[row][num] = triangle[row][num] + min(triangle[row+1][num], triangle[row+1][num+1])
        
        return triangle[0][0]




        