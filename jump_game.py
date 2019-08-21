# -*- coding: utf-8 -*-
"""
Created on August 21 2019
Leetcode: Jump Game

Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Determine if you are able to reach the last index.

Example 1:

Input: [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
Example 2:

Input: [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum
             jump length is 0, which makes it impossible to reach the last index.

Time Complexity O(n), go through array once backwards
Space Complexity: O(1), keep track of goal
@author: bohan
"""

class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        if len(nums) == 1:
            return True

        goal = len(nums) - 1
        for i in range(len(nums))[::-1]:
            if i + nums[i] >= goal:
                goal = i
        return not goal


        # Time limit exceeded
        # length = len(nums)-1
        
        # def rec(idx):
        #     if idx == length or length - idx <= nums[idx]:
        #         return True
        #     else:
        #         for i in range(1, nums[idx]+1):
        #             temp = rec(idx+i)
        #             if temp == True:
        #                 return True
        #         return False

        
        # return rec(0)