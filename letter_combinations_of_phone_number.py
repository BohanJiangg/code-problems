# -*- coding: utf-8 -*-
"""
Created on Sun Jul  7 16:19:07 2019

CTCI: Problem 16.20 - T9
Leetcode: Letter Combinations of a Phone Number

Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

Time Complexity: O(k^n), where k is the number of letters each number is mapped to (3 or 4) and n is the length of digit; alternatively (3^N * 4^M)
Space Complexity: O(k^n), need to hold all permutations in list  

@author: bohan

"""
class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        
        phoneDict = {'2':['a','b','c'], '3':['d','e','f'],'4':['g','h','i'],'5':['j','k','l'],'6':['m','n','o'],'7':['p','q','r', 's'],'8':['t','u','v'],'9':['w','x','y','z']}
        
        
        toRet = []
        for i in range(len(digits)):
            num = digits[i]
            if not toRet:
                toRet = [x for x in phoneDict[num]]
            else:
                temp = []
                for item in toRet:
                    for letter in phoneDict[num]:
                        temp.append(item[:]+letter)
                toRet = temp
        
        return toRet