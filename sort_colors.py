# -*- coding: utf-8 -*-
"""
Created on Sun Nov  4 06:26:52 2018
Leetcode: Sort Colors
Time Complexity: O(n), where n = len(nums)
Space complexity O(1), for each color
@author: bohan
"""

class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        numRed = numBlue = numWhite = 0
        
        for i in nums:
            if i == 0:
                numRed += 1
            elif i == 1:
                numWhite +=1
            elif i == 2:
                numBlue +=1
        
        for i in range(len(nums)):
            if numRed:
                nums[i] = 0
                numRed -= 1
            elif numWhite:
                nums[i] = 1
                numWhite -= 1
            elif numBlue:
                nums[i] = 2
                numBlue -=1
        
                