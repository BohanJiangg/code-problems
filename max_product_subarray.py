# -*- coding: utf-8 -*-
"""
Created on July 19 2019
Leetcode: Maximum Product Subarray

Given an integer array nums, find the contiguous subarray within an array (containing at least one number) which has the largest product.

Example 1:

Input: [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.

Time Complexity O(n), iterate through array once
Space Complexity: O(1), need to keep track of r, imax, imin
@author: bohan
"""


class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if not nums:
            return None
        
        if len(nums) == 1:
            return nums[0]

        r = nums[0]
        imax = r 
        imin = r
        for i in range(1, len(nums)):

            if nums[i] < 0:
                imax, imin = imin, imax
            

            imax = max(nums[i], nums[i] * imax)
            imin = min(nums[i], nums[i] * imin)

            r = max(r, imax)
        
        return r

        