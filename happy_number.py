# -*- coding: utf-8 -*-
"""
Created on July 22 2019
Leetcode: Happy Number

Write an algorithm to determine if a number is "happy".

A happy number is a number defined by the following process: Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers.

Example: 

Input: 19
Output: true
Explanation: 
12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1

Time Complexity O(n), iterate until the number starts repeating
Space Complexity: O(n), need to keep track of set of seen numbers 
@author: bohan
"""


class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n == 1:
            return True
        
        seen = set()
        preN = -1
        while n not in seen:
            seen.add(n)
            num = str(n)
            newN = 0
            for ch in num:
                newN += int(ch)**2
            n = newN
        return n == 1










