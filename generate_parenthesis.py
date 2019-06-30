# -*- coding: utf-8 -*-
"""
Created on Sun Jun 30 11:35:51 2019

CTCI: Problem 8.9 - Parens
Leetcode: Generate Parentheses

Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses. 

Time Complexity: O(n*max length of res), exponential time
Space Complexity: O(max length of res), 

@author: bohan

"""

class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        if n == 1:
            return ['()']
        
        # string, number of open brackets, number of completed brackets
        res = [['(',1, 0]]
        length = n*2
        
        for i in range(1,length):
            temp = []
            for item in res:
                print(item)
                if item[1] > 0:
                    temp.append([item[0]+')',item[1]-1, item[2]+1])
                if item[1] < n - item[2] and item[2] < n:
                    temp.append([item[0]+'(', item[1]+1, item[2]])
            res = temp
        
        return [x[0] for x in res]
        
            