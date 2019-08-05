# -*- coding: utf-8 -*-
"""
Created on Mon Aug  5 08:22:17 2019

Leetcode: Contains Duplicate II

Given an array of integers and an integer k, find out whether there are two distinct indices i and j in the array such that nums[i] = nums[j] and the absolute difference between i and j is at most k.

Example 1:

Input: nums = [1,2,3,1], k = 3
Output: true


Time Complexity: O(n), iterate through array once 
Space Complexity: O(k), store k elements in hash table

@author: bohan


"""


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if not nums:
            return False
        tbl = {}
        
        for i in range(len(nums)):
            if nums[i] in tbl:
                return True
            tbl[nums[i]] = i
            if len(tbl.keys())>k:
                del tbl[nums[i-k]]
        return False