# -*- coding: utf-8 -*-
"""
Created on Sun Aug 11 12:59:35 2019

Leetcode: Longest Palindromic Substring

Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example 1:

Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.

Time Complexity: O(n^2), in the worse case where the entire string is a palindrome; go through the string every time.  
Space Complexity: O(1), just need a few pointers

@author: bohan
"""

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        if not s:
            return ''
        
        res = ''
        
        def helper(l,r):
            while l >= 0 and r <len(s) and s[l] == s[r]:
                l-=1
                r+=1
            return s[l+1:r]
        
        for i in range(len(s)):
            tmp = helper(i,i)
            if len(tmp) > len(res):
                res = tmp
            tmp = helper(i, i+1)
            if len(tmp) > len(res):
                res = tmp
        
        return res
    
        
        
                    
        