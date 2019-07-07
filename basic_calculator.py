# -*- coding: utf-8 -*-
"""
Created on Sun Jul  7 15:33:53 2019

Leetcode: Basic Calculator

Implement a basic calculator to evaluate a simple expression string.

The expression string may contain open ( and closing parentheses ), the plus + or minus sign -, non-negative integers and empty spaces .

Time Complexity: O(n), 
Space Complexity: O(1), 


@author: bohan
"""

class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s.replace(" ", "")
        
        stack = []
        
        for ch in s:
            if ch in '()+-':
                stack.insert(0, ch)
            else:
                stack.insert(0, int(ch))
                
        
        opStack = []
        
        while stack:
            curr = stack.pop()
            if curr == ')':
                opStack.append(curr)
                while curr != '(':
                    curr = stack.pop()
                    opStack.append(curr)
                
                self.parensCalc(opStack)
            else:
                opStack.append(curr)
        
        
    def parensCalc(self, stack):
            num = 0
            sign = '+'
            curr = stack.pop()
            while curr != ')':
                    curr = stack.pop()
                    if curr == '+':
                        sign = '+'
                    elif curr == '-':
                        sign = '-'
                    elif curr == ')':
                        break
                    else:
                        if sign == '+':
                            num += curr
                        else:
                            num -= curr
            stack.append(num)
        
        