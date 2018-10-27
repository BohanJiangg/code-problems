# -*- coding: utf-8 -*-
"""
Created on Sat Oct 27 07:47:45 2018
Leetcode Valid Parentheses Problem.
Time Complexity: O(n). Simply iterate through stack and pop which requires O(n) time.
Space complexity: O(n). Worst Case: (((((
@author: bohan
"""

class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        paras = { ")" : "(", "}" : "{", "]":"[" }
        if len(s) == 0:
            return True
        elif len(s) % 2 == 1:
            return False
        else:
            stack = []
            pending = []
            for ch in s:
                stack.append(ch)
            
            while not len(stack) == 0:
                curr = stack.pop()
                
                if curr in paras:
                    pending.append(paras[curr])
                elif len(pending) == 0 or pending.pop() != curr:
                    return False
                
            return True