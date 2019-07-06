# -*- coding: utf-8 -*-
"""

CTCI: Problem 10.8 - Find Duplicates (Similar)
Leetcode: Find the Duplicate Number

Given an array nums containing n + 1 integers where each integer is between 1 and n (inclusive), prove that at least one duplicate number must exist. Assume that there is only one duplicate number, find the duplicate one.

Note:

    You must not modify the array (assume the array is read only).
    You must use only constant, O(1) extra space.
    Your runtime complexity should be less than O(n2).
    There is only one duplicate number in the array, but it could be repeated more than once.


Time Complexity: O(n log n), need to sort array.
Space Complexity: O(n), timsort space complexity 


For O(n) time complexity and O(1) space complexity, use tortoise and hare and solve like linked list 2.


@author: bohan

"""

class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        if len(nums) == 2:
            return nums[0]
        
        nums = sorted(nums)
        
        prev = nums[0]        
        for i in range(1, len(nums)):
            if nums[i] == prev:
                return prev
            prev = nums[i]