# -*- coding: utf-8 -*-
"""
Created on Wed Jul 10 20:35:41 2019

Leetcode: Minimum Size Subarray Sum

Given an array of n positive integers and a positive integer s, find the minimal length of a contiguous subarray of which the sum ≥ s. If there isn't one, return 0 instead.

Time Complexity: O(n), iterate through array once 
Space Complexity: O(n), need to keep track of curr, left, length as  constants. 

@author: bohan

"""

class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        
        if not nums:
            return 0
        if len(nums) == 1:
            return 1
        
    
        curr = 0
        left = 0
        length = len(nums)+1
        
        for i, num in enumerate(nums):
            curr += num
            
            while curr >= s:
                length = min(length, i-left+1)
                curr = curr - nums[left]
                left += 1
                
        return length if length <= len(nums) else 0
            
            
            
            
            
            
            
            
            
            