# -*- coding: utf-8 -*-
"""
Created on Sat Jun 29 14:53:05 2019

CTCI: Problem 8.4 - Power Set 
Leetcode: Subsets II

Given a collection of integers that might contain duplicates, nums, return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.

Time Complexity: O(n)
Space Complexity: O(1)

@author: bohan
"""

class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        power_set = []
        
        for i in range(len(nums)):
            set = []
            for j in range(i, len(nums)):
    
    def recursive_sub(self, nums):
        if not nums:
            return []
        