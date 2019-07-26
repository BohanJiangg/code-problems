# -*- coding: utf-8 -*-
"""
Created on Sun Jun 30 10:43:16 2019

CTCI: Problem 8.8 - Permutations with Dups
Leetcode: Permutations II

Given a collection of numbers that might contain duplicates, return all possible unique permutations.

Example:

Input: [1,1,2]
Output:
[
  [1,1,2],
  [1,2,1],
  [2,1,1]
]


Time Complexity: O(n), 
Space Complexity: O(1), 

@author: bohan

"""


class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
