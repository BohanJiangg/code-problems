# -*- coding: utf-8 -*-
"""
Created on Sat Jul  6 15:26:52 2019

CTCI: Problem 10.3
Leetcode: Search in Rotated Sorted Array

Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).

You are given a target value to search. If found in the array return its index, otherwise return -1.

You may assume no duplicate exists in the array.

Your algorithm's runtime complexity must be in the order of O(log n).

Time Complexity: O(log(n)), only goes through half the array  
Space Complexity: O(1), keeps track of flags and constants 

@author: bohan

"""

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        if not nums:
            return -1
        
        if len(nums) == 1 and nums[0] != target:
            return -1
        
        first = nums[0]
        last = nums[-1]
        
        
        if target == first:
            return 0
        if target == last:
            return len(nums) -1
        
        
        if abs(first - target) < abs(last-target):
            isGreater = True
            if first-target < 0:
                isGreater = False
            
            for idx in range(1, len(nums)):
                if nums[idx] == target:
                    return idx
                elif isGreater and nums[idx] < target:
                    return -1
                elif not isGreater and nums[idx] > target:
                    return -1
            return -1
            
        else:
            isGreater = True
            if last-target < 0:
                isGreater = False
            for idx in range (len(nums)-2, -1, -1):
                if nums[idx] == target:
                    return idx
                elif isGreater and nums[idx] < target:
                    return -1
                elif not isGreater and nums[idx] > target:
                    return -1
            return -1
        