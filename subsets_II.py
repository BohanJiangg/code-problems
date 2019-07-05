# -*- coding: utf-8 -*-
"""
Created on Sat Jun 29 14:53:05 2019

CTCI: Problem 8.4 - Power Set 
Leetcode: Subsets II

Given a collection of integers that might contain duplicates, nums, return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.

Time Complexity: O(n^2), loop through nums at most n^2 if no dupes
Space Complexity: O(n^2), if no dupes

@author: bohan
"""

class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = [[]]
        nums.sort()
        for i in range(len(nums)):
            if i == 0 or nums[i] != nums[i - 1]:
                l = len(res)
            for j in range(len(res) - l, len(res)):
                res.append(res[j] + [nums[i]])
        return res