# -*- coding: utf-8 -*-
"""
Created on Sun Jul 21 15:30:13 2019
Leetcode: Evaluate Reverse Polish Notation

Evaluate the value of an arithmetic expression in Reverse Polish Notation.

Valid operators are +, -, *, /. Each operand may be an integer or another expression.

Note:
    Division between two integers should truncate toward zero.
    The given RPN expression is always valid. That means the expression would always evaluate to a result and there won't be any divide by zero operation.


Time Complexity O(n), iterate through list once
Space Complexity: O(n), need stack to keep track of operands
@author: bohan
"""

class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        
        if not tokens:
            return None
        
        stack = []
        
        for item in tokens:
            if item in "+-*/":
                # deque and do something
                
                op2 = stack.pop(0)
                op1 = stack.pop(0)
                if item == "+":
                    stack.insert(0,op1+op2)
                elif item == "-":
                    stack.insert(0,op1-op2)
                elif item == "*":
                    stack.insert(0,op1*op2)
                else:
                    stack.insert(0, int(op1/float(op2)) )

            else:
                stack.insert(0, int(item))
            
        
        return stack.pop(0)