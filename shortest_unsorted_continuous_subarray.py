# -*- coding: utf-8 -*-
"""
Created on Sun Jul  7 14:56:58 2019

CTCI: Problem 16.16 - Sub Sort
Leetcode: Shortest Unsorted Continuous Subarray

Given an integer array, you need to find one continuous subarray that if you only sort this subarray in ascending order, then the whole array will be sorted in ascending order, too.

You need to find the shortest such subarray and output its length.

Time Complexity: O(n log n), need to sort array 
Space Complexity: O(n), need to clone array 

@author: bohan

"""

class Solution(object):
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        if len(nums) == 1:
            return 0
        
        sortedNums = sorted(nums)
        
        startIdx = len(nums) -1
        endIdx = 0
        
        for i in range(len(sortedNums)):
            if sortedNums[i] != nums[i]:
                startIdx = min(startIdx, i)
                endIdx = max(endIdx, i)
        
        
        if endIdx - startIdx >= 0:
            
            return endIdx - startIdx + 1
        else:
            return 0 