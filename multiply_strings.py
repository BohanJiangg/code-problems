# -*- coding: utf-8 -*-
"""
Created on September 1, 2019
Leetcode: Multiply Strings

Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2, also represented as a string.

Example 1:

Input: num1 = "2", num2 = "3"
Output: "6"

Example 2:

Input: num1 = "123", num2 = "456"
Output: "56088"

Note:

    The length of both num1 and num2 is < 110.
    Both num1 and num2 contain only digits 0-9.
    Both num1 and num2 do not contain any leading zero, except the number 0 itself.
    You must not use any built-in BigInteger library or convert the inputs to integer directly.

Time Complexity: O(n), iterate through num1 and num2 once each
Space Complexity: O(1), keep adding onto int1 and int2

@author: bohan

"""

class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        
        if not num1:
            return num2
        if not num2:
            return num1
        
        if num1 == '0' or num2 == '0':
            return '0'
        
        mul = 1
        int1 = 0 
        for i in range(len(num1)-1, -1, -1):
            int1 += mul * int(num1[i])
            mul *= 10
        
        mul = 1
        int2 = 0 
        for i in range(len(num2)-1, -1, -1):
            int2 += mul * int(num2[i])
            mul *= 10
        
        return str(int1*int2)
        
        
            

        