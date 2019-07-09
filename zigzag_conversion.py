# -*- coding: utf-8 -*-
"""
Created on Mon Jul  8 20:39:00 2019

Leetcode: ZigZag Conversion

The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R

And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string s, int numRows);

Time Complexity: O(n), iterate through string once
Space Complexity: O(n), need lists to support entire string

@author: bohan

"""

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        
        if numRows == 1:
            return s
        lists = []
        for i in range(numRows):
            lists.append([])
        
        toggle = 1
        rowIdx = 0
        for i in range(len(s)):
            
            lists[rowIdx].append(s[i])
            
            if rowIdx == numRows-1:
                toggle *= -1
            if rowIdx == 0 and i != 0:
                toggle *= -1
            
            rowIdx += toggle
        
        s = ''
        for lis in lists:
            s = s + ''.join(lis)
            
        return s
            