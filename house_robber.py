# -*- coding: utf-8 -*-
"""
Created on Sun Jul 21 15:47:18 2019
Leetcode: House Robber

You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security system connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.

Time Complexity O(n), iterate through array once
Space Complexity: O(1), 2 pointers
@author: bohan
"""

class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        
        prevMax = currMax = 0
        for num in nums:
            temp = currMax
            currMax = max(prevMax+num, currMax)
            prevMax = temp
        
        
        return currMax
    