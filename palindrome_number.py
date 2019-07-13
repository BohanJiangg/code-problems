# -*- coding: utf-8 -*-
"""
Created on Sat Jul 13 17:06:52 2019
Leetcode: Palindrome Number

Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.

Time Complexity O(n), iterate through half the string 
Space Complexity: O(n), need to convert int to string 
@author: bohan
"""

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        
        if x < 0:
            return False
        
        if len(str(x)) == 1:
            return True
        
        
        strNum = str(x)
        half = int(len(strNum)/2) 
        
        for i in range(half):
            if strNum[i] != strNum[len(strNum) - i - 1]:
                return False
        return True
    
                
                
        
        
        
        