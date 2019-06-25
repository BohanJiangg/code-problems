# -*- coding: utf-8 -*-
"""
Created on Tues June 04 2019

Leetcode: Wiggle Sort II

Given an unsorted array nums, reorder it such that nums[0] < nums[1] > nums[2] < nums[3]....

Example 1:

Input: nums = [1, 5, 1, 1, 6, 4]
Output: One possible answer is [1, 4, 1, 5, 1, 6].

Time Complexity: O(n), 
Space Complexity: O(n), 

@author: bohan
"""

class Solution(object):
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        O(n) time, O(1) extra space?
        """

        '''
        Solution by finding median and using O(nlogn) time (due to sort) and O(1) space
        '''
        nums.sort()
        
        half = len(nums[::2]) - 1
       
        # even indexes, odd indexes = small, large
        nums[0::2], nums[1::2] = nums[half::-1], nums[:half:-1]
        



        '''
        Solution by finding median in O(n log n) time (due to sort) and O(n) space because two additional lists are needed
        '''
        sortedNums = sorted(nums)

        if len(sortedNums) % 2 == 0:
            idx2 = len(sortedNums)/2 
            median = (sortedNums[idx2] + sortedNums[idx2 - 1])/2
            stopAt = len(sortedNums) / 2 - 1
        else:
            median = sortedNums[len(sortedNums)/2]
            stopAt = len(sortedNums) /2

        
        smallNums = []
        largeNums = []
        for i in range(len(sortedNums)):
            
            if sortedNums[i] <= median and i <= stopAt:
                smallNums.append(sortedNums[i])
            else:
                largeNums.append(sortedNums[i])

        for i in range(len(nums)):
            if i % 2 ==0:
                nums[i] = smallNums.pop()
            else:
                nums[i] = largeNums.pop()
        





