# -*- coding: utf-8 -*-
"""
Created on July 15 2019
Leetcode: Reverse Words in a String III

Given a string, you need to reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.

Example 1:
Input: "Let's take LeetCode contest"
Output: "s'teL ekat edoCteeL tsetnoc"
Note: In the string, each word is separated by single space and there will not be any extra space in the string.

Time Complexity O(n), loop through string and store in stack till next whitespace
Space Complexity: O(n), need stack and another string 
@author: bohan
"""

class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        toRet = ''
        stack = []
        for ch in s:
            if ch == " ":
                while stack:
                    toRet += stack.pop(-1)
                toRet += " "
            else:
                stack.append(ch)

        while stack:
                    toRet += stack.pop(-1)

        return toRet
        