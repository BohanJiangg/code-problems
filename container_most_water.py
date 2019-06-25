# -*- coding: utf-8 -*-
"""
Created on May 24 2019
Leetcode: Container With Most Water

Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis forms a container, such that the container contains the most water.

Note: You may not slant the container and n is at least 2.

Ex.:                                             
Input: [1,8,6,2,5,4,8,3,7]
Output: 49


Time Complexity O(n), one pass with two pointers 
Space Complexity: O(1), need only three constants to track maxArea
@author: bohan
"""


class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if not height:
            return 0
        leftptr = 0
        rightptr = len(height) - 1
        maxArea = min(height[leftptr], height[rightptr]) * (rightptr - leftptr)

        while leftptr != rightptr:
            if min(height[leftptr], height[rightptr]) * (rightptr - leftptr) > maxArea:
                maxArea = min(height[leftptr], height[rightptr]) * (rightptr - leftptr)
            
            if height[leftptr] < height[rightptr]:
                leftptr += 1
            else:
                rightptr -= 1
        
        return maxArea
