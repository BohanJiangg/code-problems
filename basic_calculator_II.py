# -*- coding: utf-8 -*-
"""
Created on August 12 2019    
Leetcode: Basic Calculator II

Implement a basic calculator to evaluate a simple expression string.

The expression string contains only non-negative integers, +, -, *, / operators and empty spaces . The integer division should truncate toward zero.

Example 1:

Input: "3+2*2"
Output: 7

Time Complexity O(n), iterate through array once
Space Complexity: O(n), keep track of digits through stack
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
        num, stack, sign = 0, [], "+"
        for i in range(len(s)):
            if s[i].isdigit():
                num = num * 10 + int(s[i])
            if s[i] in "+-*/" or i == len(s) - 1:
                if sign == "+":
                    stack.append(num)
                elif sign == "-":
                    stack.append(-num)
                elif sign == "*":
                    stack.append(stack.pop()*num)
                else:
                    prev = stack.pop()
                    if prev < 0 or num < 0:
                        stack.append(-int(abs(prev)/abs(num)))
                    else:
                        stack.append(int(prev/num))
                num = 0
                sign = s[i]
        return sum(stack)






