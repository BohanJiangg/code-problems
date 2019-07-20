# -*- coding: utf-8 -*-
"""
Created on Sat Jul 20 16:07:35 2019
Leetcode: Maximum Subarray

Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.
Example:

    Input: [-2,1,-3,4,-1,2,1,-5,4],
    Output: 6
    Explanation: [4,-1,2,1] has the largest sum = 6.


Time Complexity O(n), iterate through array once
Space Complexity: O(1), need currSum and maxSum 
@author: bohan
"""


class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        else:
            currSum = maxSum = nums[0]
            for i in range(1, len(nums)):
                currSum = max(nums[i], currSum + nums[i])
                maxSum = max(maxSum, currSum)
                
          
            return maxSum
            
            