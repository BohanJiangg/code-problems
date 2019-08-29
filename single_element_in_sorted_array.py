# -*- coding: utf-8 -*-
"""
Created on August 29 2019
Leetcode: Single Element in a Sorted Array

Given a sorted array consisting of only integers where every element appears exactly twice except for one element which appears exactly once. Find this single element that appears only once.


Example 1:

Input: [1,1,2,3,3,4,4,8,8]
Output: 2

Example 2:

Input: [3,3,7,7,10,11,11]
Output: 10

Note: Your solution should run in O(log n) time and O(1) space.



Time Complexity: O(n), iterate through nums once
Space Complexity: O(1), no extra storage needed

@author: bohan

"""

class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:

        if not nums:
            return None
        if len(nums) == 1:
            return nums[0]
        
        
        for i in range(0, len(nums)-1, 2):
            if not nums[i] == nums[i+1]:
                return nums[i]      

        return nums[-1]  
            

        