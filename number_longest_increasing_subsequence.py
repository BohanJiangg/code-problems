# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 10:30:39 2019
Leetcode: Number of Longest Increasing Subsequence

 Given an unsorted array of integers, find the number of longest increasing subsequence.

Example 1:

Input: [1,3,5,4,7]
Output: 2
Explanation: The two longest increasing subsequence are [1, 3, 4, 7] and [1, 3, 5, 7].

Example 2:

Input: [2,2,2,2,2]
Output: 5
Explanation: The length of longest continuous increasing subsequence is 1, and there are 5 subsequences' length is 1, so output 5.


Time Complexity: O(n^2), go through the array twice for each index 
Space Complexity: O(n), memoize longest increasing subsequence at each index and count of the longest increasing subsequence at each index


@author: bohan
"""

class Solution(object):
    def findNumberOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        if not nums:
            return 0
        
        dp = [0] * (len(nums))       
        counts = [1] * (len(nums))
        
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    if dp[j] >= dp[i]:
                        dp[i] = 1+dp[j]
                        counts[i] = counts[j]
                    elif dp[j] + 1 == dp[i]:
                        counts[i] += counts[j]
        
        
        longest = max(dp)
        
        return sum(c for i, c in enumerate(counts) if dp[i] == longest)
    
        
        