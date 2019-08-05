# -*- coding: utf-8 -*-
"""
Created on Mon Aug  5 08:18:15 2019

Leetcode: Contains Duplicate

Given an array of integers, find if the array contains any duplicates.

Your function should return true if any value appears at least twice in the array, and it should return false if every element is distinct.

Example 1:

Input: [1,2,3,1]
Output: true

Time Complexity: O(1), convert list to set and check lengths
Space Complexity: O(n), convert list to set 

@author: bohan


"""


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return False if len(set(nums)) == len(nums) else True
    