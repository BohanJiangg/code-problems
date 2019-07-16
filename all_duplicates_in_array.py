# -*- coding: utf-8 -*-
"""
Created on Mon Jul 15 19:31:25 2019
Leetcode: Find All Duplicates in an Array

Given an array of integers, 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.

Find all the elements that appear twice in this array.

Could you do it without extra space and in O(n) runtime?

Time Complexity O(n), iterate through array once
Space Complexity: O(1), keep track of dupes using negative sign at index
@author: bohan
"""

class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        res = []
        
        for i in range(len(nums)):
            if nums[abs(nums[i])-1] >= 0:
                nums[abs(nums[i])-1] *= -1
            else:
                res.append(abs(nums[i]))
        
        
        return res