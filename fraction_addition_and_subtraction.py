# -*- coding: utf-8 -*-
"""
Created on Sun Jul 14 16:50:59 2019
Leetcode: Fraction to Recurring Decimal

Given two integers representing the numerator and denominator of a fraction, return the fraction in string format.

If the fractional part is repeating, enclose the repeating part in parentheses.

Time Complexity O(n), 
Space Complexity: O(1), 
@author: bohan
"""


class Solution(object):
    def fractionAddition(self, expression):
        """
        :type expression: str
        :rtype: str
        """
        if not expression:
            return ''
        
        first = ''
        second = ''
        isFirst = True
        signList = []
        floatList = []
        
        
        
        first = first + expression[0]
        
        for i in range(1, len(expression)):
            ch = expression[i]
            
            if ch == '/':
                isFirst = False
                # do something
            elif ch in '+-':
                # do something
                signList.append(ch)
                floatList.append(float(first)/float(second))
                isFirst = True
                first = ''
                second = ''
                
            else:
                if isFirst:
                    first += ch
                else:
                    second += ch
        
        floatList.append(float(first)/float(second))
            
        
        ans = 0
        while signList:
            sign = signList.pop(0)
            num1 = floatList.pop(0)
            num2 = floatList.pop(0)
            
            if sign == '+':
                ans = num1+num2
            else:
                ans = num1-num2
            floatList.insert(0, ans)
            
        if ans == 0:
            return '0/1'
        
        ints = ans.as_integer_ratio()
        return str(ints[0]) + '/'+str(ints[1])
        
        
        
        
        
        
        
        
        
        
        