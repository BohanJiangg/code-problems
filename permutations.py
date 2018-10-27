# -*- coding: utf-8 -*-
"""
Created on Sat Oct 27 07:49:15 2018
Leetcode: Permutations


@author: bohan
"""

class Solution:
    
    def permuteRecursive(self, nums):
        if len(nums) == 2:
            return [nums, [nums[1],nums[0]]]
        else:
            rest = self.permuteRecursive(nums[1:])
            
            results = []
            
            for listNums in rest:
                for i in range(0, len(listNums)+1):
                    temp = listNums.copy()
                    temp.insert(i, nums[0])
                    results.append(temp)
                    
            return results
        
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) >= 2:
            return self.permuteRecursive(nums)
        else:
            return [nums]
        