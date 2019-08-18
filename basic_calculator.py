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
        if not s:
            return None
        
        
        s = s.replace(" ", "")
        
        numStk = []
        opStk = []
        prevDigit = False
        openList = []
        for ch in s:
            if ch in '+-':
                opStk.append(ch)
                prevDigit = False
            elif ch.isdigit():
                if prevDigit:
                    numStk.append(int(str(numStk.pop(-1))+ch))
                else:
                    numStk.append(int(ch))
                    prevDigit = True
            elif ch == '(':
                numStk.append(ch)
                prevDigit = False
                openList.append(len(numStk)-1)
            else:
                # ch == ')'
                start = openList.pop(-1)
                numStk.pop(start)
                
                for i in range(start, len(numStk)):
                    first = numStk.pop(0)
            second = numStk.pop(0)
            op = opStk.pop(0)
                
                
                curr = numStk.pop(-1)
                while numStk[-1] != '(':
                    first = numStk.pop(-1)
                    op = opStk.pop(-1)
                    if op == '+':
                        curr = first + curr
                    else:
                        curr = first - curr
                numStk.pop(-1)
                numStk.append(curr)
        
        while len(numStk) > 1:
            first = numStk.pop(0)
            second = numStk.pop(0)
            op = opStk.pop(0)
            if op == '+':
                curr = first + second
            else:
                curr = first - second
            numStk.insert(0, curr)
        
        return numStk.pop()
        
    
        