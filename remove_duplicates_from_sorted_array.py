# -*- coding: utf-8 -*-
"""
Created on Sat Aug  3 19:48:08 2019
Leetcode: Remove Duplicates from Sorted Array

Given a sorted array nums, remove the duplicates in-place such that each element appear only once and return the new length.

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

Time Complexity: O(n), one-pass
Space Complexity: O(n), constant since elements are swapped.

@author: bohan

"""

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        if not nums:
            return 0
        
        idx = 1
        prev = nums[0]
        for i in range(1, len(nums)):
            if nums[i] != prev:
                prev = nums[i]
                nums[idx], nums[i] = nums[i], nums[idx]
                idx += 1
                
        nums = nums[:idx]
        
        return idx