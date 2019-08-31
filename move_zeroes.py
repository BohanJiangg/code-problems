# -*- coding: utf-8 -*-
"""
Created on August 31 2019
Leetcode: Move Zeroes

Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Example:

Input: [0,1,0,3,12]
Output: [1,3,12,0,0]

Note:

    You must do this in-place without making a copy of the array.
    Minimize the total number of operations.


Time Complexity: O(n), iterate through array once
Space Complexity: O(1), in-place 

@author: bohan

"""

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        if not nums:
            return 
        
        length = len(nums)
        idx = 0
        for i in range(length):
            if nums[idx] == 0:
                nums.pop(idx)
                nums.append(0)
                idx -=1
            idx +=1

      

        