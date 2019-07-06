# -*- coding: utf-8 -*-
"""
Created on Sun Jun 30 10:43:16 2019

CTCI: Problem 8.8 - Permutations with Dups
Leetcode: Permutations II

Given a collection of numbers that might contain duplicates, return all possible unique permutations.

Time Complexity: O(n), one loop to go through every n
Space Complexity: O(1), only need to keep 3 constants.

@author: bohan

"""


class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        