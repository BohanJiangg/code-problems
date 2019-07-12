# -*- coding: utf-8 -*-
"""
Created on July 12 2019
Leetcode: Two Sum

Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].

Time Complexity O(n), one-pass hash table 
Space Complexity: O(n), need to store num complements in hash table.  
@author: bohan
"""

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        # One pass hash table solution
        tbl = {}
        
        for i in range(len(nums)):
            if nums[i] in tbl:
                return [tbl[nums[i]], i]
            complement = target - nums[i]
            tbl[complement] = i
        
        return -1 





        # Slow O(n^2) brute force solution 
        # complement = []
        # for i in nums:
        #     complement.append(target - i)
        
        # for i in range(len(complement)):
        #     if complement[i] in nums:
        #         tgt_idx = nums.index(complement[i])
        #         if tgt_idx != i:
        #             return [i, tgt_idx]
        
        # return -1

        
        