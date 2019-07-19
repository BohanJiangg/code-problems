# -*- coding: utf-8 -*-
"""
Created on Thu Jul 18 20:23:13 2019
Leetcode: 3Sum

Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note:

The solution set must not contain duplicate triplets.

Example:

Given array nums = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]


Time Complexity O(n^2), iterate through nums once and then iterate through nums again in while loop 
Space Complexity: O(N), array to store 3sums
@author: bohan
"""

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        res = []
        nums.sort()
        
        length = len(nums)
        
        for i in range(length-2):
            
            if nums[i] > 0:
                break
            if i > 0 and nums[i-1] == nums[i]:
                continue
            
            l, r = i +1, length - 1
            while l < r:
                total = nums[i] + nums[l] + nums[r]
                
                if total < 0:
                    l += 1
                elif total >0:
                    r -= 1
                else:
                    res.append([nums[i], nums[l], nums[r]])
                    
                    while l<r and nums[l] == nums[l+1]:
                        l+=1
                    while r>l and nums[r] == nums[r-1]:
                        r-=1
                    
                    l+=1
                    r-=1
        
        return res
        
    #-3, 1, 1, 2, 2
        
        
        
        
        
        
        
        
        
        
        
        