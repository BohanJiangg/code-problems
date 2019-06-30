# -*- coding: utf-8 -*-
"""
Created on Sun Jun 30 16:37:38 2019

Leetcode: Combination Sum

Given a set of candidate numbers (candidates) (without duplicates) and a target number (target), find all unique combinations in candidates where the candidate numbers sums to target.

The same repeated number may be chosen from candidates unlimited number of times.

Note:

    All numbers (including target) will be positive integers.
    The solution set must not contain duplicate combinations.


Time Complexity: O(len(candidates)^(target/min(candidates)))
Space Complexity: O(target/min(candidates)), size of max call stack

@author: bohan

"""

class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        
        ret = []
        
        def dfs(curr, path, index):
            if curr < 0:
                return
            if curr == 0:
                ret.append(path)
                return
            for i in range(index, len(candidates)):
                dfs(curr-candidates[i], path+[candidates[i]], i)
        
        dfs(target, [], 0)
                    
            
        
        
        return ret 
        
        
    
        