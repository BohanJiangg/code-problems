# -*- coding: utf-8 -*-
"""
Created on Sat Jul 27 11:25:06 2019
Leetcode: Single Number II

Given a non-empty array of integers, every element appears three times except for one, which appears exactly once. Find that single one.

Note:

Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Example 1:

Input: [2,2,3,2]
Output: 3

Example 2:

Input: [0,1,0,1,0,1,99]
Output: 99


Time Complexity: O(n), loop through nums once
Space Complexity: O(n), keep track of candidates and previously seen numbers  

@author: bohan

"""

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        prev = {}
        candidates = {}
        for num in nums:
            if not num in prev and not num in candidates:
                candidates[num] = 1
            elif num in candidates:
                prev[num] = 1
                del candidates[num]
                
        return candidates.keys()[0]