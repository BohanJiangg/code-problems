# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 09:58:29 2019
Leetcode: Longest Increasing Subsequence

Given an unsorted array of integers, find the length of longest increasing subsequence.

Example:

Input: [10,9,2,5,3,7,101,18]
Output: 4 
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4. 

Note:

    There may be more than one LIS combination, it is only necessary for you to return the length.
    Your algorithm should run in O(n2) complexity.


Time Complexity: O(n^2), go through the array twice for each index 
Space Complexity: O(n), memoize longest increasing subsequence at each index


@author: bohan
"""

class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        if not nums:
            return 0
        
        dp = [1] + [0] * (len(nums) -1)       
        for i in range(1, len(nums)):
            
            curr = 1
            for j in range(i):
                if nums[i] > nums[j]:
                    curr = max(curr, 1+ dp[j])
            
            dp[i] = curr
                  
                    
            
        
        return max(dp)