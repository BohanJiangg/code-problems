# -*- coding: utf-8 -*-
"""
Created on Mon Jun 24 19:57:11 2019

Leetcode: Top K Frequent Elements

Given a non-empty array of integers, return the k most frequent elements.

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]


Time Complexity: O(nlogn) time, need to sort the items in nums
Space Complexity: O(n), Need a list containing all the distinct nums and frequency 

@author: bohan

"""

class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        if not nums:
            return None
        
        if k == len(nums):
            return nums
        
        nums = sorted(nums)
        
        
        list_nums = []
        x = nums[0]
        curr = [x, 1]
        
        for i in range(len(nums)):
            if nums[i] == x:
                curr[1] += 1
                
            else:
                x = nums[i]
                list_nums.append(curr)
                curr = [x, 1]
            
            if i == len(nums) - 1:
                    list_nums.append(curr)
        
        list_nums = sorted(list_nums, key=lambda x: x[1])
        
        toRet = []
        
        while k != 0 and list_nums:
            toRet.append(list_nums.pop(-1)[0])
            k -= 1
        
        return toRet
       
        
        
        
        
        