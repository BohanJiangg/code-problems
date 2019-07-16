# -*- coding: utf-8 -*-
"""
Created on July 16 2019
Leetcode: Find First and Last Position of Element in Sorted Array

Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].

Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]

Time Complexity O(log n) time on average (start from closer pointer), but O(n) where entire nums array is = target
Space Complexity: O(1), 2 ptrs to keep track of range of target 
@author: bohan
"""

class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        toRet = [-1, -1]
        if not nums:
            return toRet
        if len(nums) == 1 and nums[0] != target:
            return toRet
        elif len(nums) == 1 and nums[0] == target:
            return [0, 0]

        startIdx = 0
        if abs(nums[0] - target) >  abs(nums[len(nums)-1] - target):
            startIdx = len(nums) - 1
       
        ptr1 = -1
        ptr2 = -1

        if startIdx == 0:
            while startIdx < len(nums) and nums[startIdx] <= target:
                if nums[startIdx] == target:
                    if ptr1 == -1:
                        ptr1 = startIdx
                    ptr2 = startIdx
                startIdx += 1
            return [ptr1, ptr2]
        else:
            while startIdx > 0 and nums[startIdx] >= target:
                if nums[startIdx] == target:
                    if ptr1 == -1:
                        ptr1 = startIdx
                    ptr2 = startIdx
                startIdx -= 1
            return[ptr2, ptr1]