# -*- coding: utf-8 -*-
"""
Created on Mon Aug  5 08:56:26 2019

Leetcode: Longest Valid Parentheses

Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.

Example 1:

Input: "(()"
Output: 2
Explanation: The longest valid parentheses substring is "()"

Example 2:

Input: ")()())"
Output: 4
Explanation: The longest valid parentheses substring is "()()"


Time Complexity: O(n), one-pass 
Space Complexity: O(n), store paraentheses in stack

@author: bohan
"""

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        
        if not s:
            return 0
        
        stack = [-1]
        maxLength = 0
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            else:
                stack.pop(-1)
                if not stack:
                    stack.append(i)
                else:
                    
                    maxLength = max(maxLength, i-stack[-1])
        return maxLength
            