
# -*- coding: utf-8 -*-
"""
Created on August 23 2019
Leetcode: Max Consecutive Ones II

Given a binary array, find the maximum number of consecutive 1s in this array if you can flip at most one 0.

Example 1:
Input: [1,0,1,1,0]
Output: 4
Explanation: Flip the first zero will get the the maximum number of consecutive 1s.
    After flipping, the maximum number of consecutive 1s is 4.
Note:

The input array will only contain 0 and 1.
The length of input array is a positive integer and will not exceed 10,000

Time Complexity O(n), iterate through array once
Space Complexity: O(1), keep track of 3 variables
@author: bohan
"""

class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        if not nums:
            return 0
        
        
        pre, curr, maxLen = -1, 0, 0

        for i in nums:
            if i == 0:
                pre, curr = curr, 0
            else:
                curr+=1
            
            maxLen = max(maxLen, pre+1+curr)
        return maxLen