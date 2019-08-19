# -*- coding: utf-8 -*-
"""
Created on August 19 2019
Leetcode: 3Sum Closest

Given an array nums of n integers and an integer target, find three integers in nums such that the sum is closest to target. Return the sum of the three integers. You may assume that each input would have exactly one solution.

Example:

Given array nums = [-1, 2, 1, -4], and target = 1.

The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).


Time Complexity O(n), 
Space Complexity: O(1), 
@author: bohan
"""

class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """


        # Working but too slow
        # nums.sort()

        # tbl = {}

        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         tbl[(i,j)] = nums[i] + nums[j]
        
        # closest = toRet = float('inf')
        
        # for i in range(len(nums)):
        #     for key, val in tbl.items():
        #         if not i in key:
        #             if abs(target - (val+nums[i])) < closest:
        #                 toRet = val+nums[i]
        #                 closest = abs(target - (val+nums[i])) 
        
        # return toRet
