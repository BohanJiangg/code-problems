# -*- coding: utf-8 -*-
"""
Created on Sun Jul 21 14:50:27 2019
Leetcode: Wiggle Sort

Given an unsorted array nums, reorder it in-place such that nums[0] <= nums[1] >= nums[2] <= nums[3]....

Time Complexity O(n), pass through array once
Space Complexity: O(1), nums sorted in-place
@author: bohan
"""



class Solution(object):
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        
        
        for i in range(len(nums)):
            if i % 2 == 0:
                # this should be a small number
                if i+1 < len(nums) and nums[i] > nums[i+1]:
                    nums[i], nums[i+1] = nums[i+1], nums[i]
                
            else:
                # this should be a large number
                if i + 1 < len(nums) and nums[i] < nums[i+1]:
                    nums[i], nums[i+1] = nums[i+1], nums[i]
        
        
        
        
        # O(n log n) method using sorted array
#        nums.sort()
#        
#        for i in range(1, len(nums), 2):
#            if i+1 < len(nums):
#                nums[i], nums[i+1] = nums[i+1], nums[1]
    
        
        