# -*- coding: utf-8 -*-
"""
Created on Sat Aug  3 15:23:53 2019
Leetcode: Implement strStr()

Implement strStr().

Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Example 1:

Input: haystack = "hello", needle = "ll"
Output: 2


Time Complexity: O(n), iterate through haystack once
Space Complexity: O(1), just return index 

@author: bohan

"""

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0

        for i in range(len(haystack) - len(needle)+1):
            if haystack[i:i+len(needle)] == needle:
                return i

        return -1