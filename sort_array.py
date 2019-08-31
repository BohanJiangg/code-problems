# -*- coding: utf-8 -*-
"""
Created on August 31 2019
Leetcode: Sort an Array

Given an array of integers nums, sort the array in ascending order.

Example 1:

Input: [5,2,3,1]
Output: [1,2,3,5]

Example 2:

Input: [5,1,1,2,0,0]
Output: [0,0,1,1,2,5]

Time Complexity: O(n log n), built-in timsort
Space Complexity: O(n), timsort space complexity

@author: bohan

"""
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        nums.sort()
        return nums