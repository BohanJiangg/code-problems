# -*- coding: utf-8 -*-
"""
Created on Tues June 04 2019

Leetcode: Wiggle Sort II

Given an unsorted array nums, reorder it such that nums[0] < nums[1] > nums[2] < nums[3]....

Example 1:

Input: nums = [1, 5, 1, 1, 6, 4]
Output: One possible answer is [1, 4, 1, 5, 1, 6].

Time Complexity: O(n), 
Space Complexity: O(n), 

@author: bohan
"""

class Solution(object):
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        O(n) time, O(1) extra space?
        """
        

        for i in range(len(nums)):
            
            ptr1 = i
            ptr2 = len(nums) - (i+1)

            if ptr1 > ptr2:
                break
            
            

            
            # if position is even, this is a small integer
            if i % 2 == 0:
                # Check if next number is smaller or equal to current number
                if i - 1 > 0:
                    if nums[i+1] <= nums[i]:
                        # if so, swap with next larger integer.
                        

            # if position is odd, this is a large integer
            else:









