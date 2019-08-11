# -*- coding: utf-8 -*-
"""
Created on Sun Aug 11 11:54:29 2019

Range Sum Query - Immutable

Given an integer array nums, find the sum of the elements between indices i and j (i ≤ j), inclusive.

Example:

Given nums = [-2, 0, 3, -5, 2, -1]

sumRange(0, 2) -> 1
sumRange(2, 5) -> -1
sumRange(0, 5) -> -3


Time Complexity: O(n), one-pass for prefix sums calculation
Space Complexity: O(n), need to store prefix-sums array

@author: bohan
"""
class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        if not nums:
            self.prefix_sums = []
        else:
            self.prefix_sums = [nums[0]] + [0] * (len(nums) - 1)
            for i in range(1, len(nums)):
                self.prefix_sums[i] = self.prefix_sums[i-1] + nums[i] 

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        if i == 0:
            return self.prefix_sums[j]
        else:    
            return self.prefix_sums[j] - self.prefix_sums[i-1]
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)