# -*- coding: utf-8 -*-
"""
Created on August 7 2019    
Leetcode: Decode String

Given an encoded string, return its decoded string.

The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.

You may assume that the input string is always valid; No extra white spaces, square brackets are well-formed, etc.

Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. For example, there won't be input like 3a or 2[4].

Examples:

s = "3[a]2[bc]", return "aaabcbc".
s = "3[a2[c]]", return "accaccacc".
s = "2[abc]3[cd]ef", return "abcabccdcdcdef".

Time Complexity O(n), 
Space Complexity: O(1), 
@author: bohan
"""

class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """

        if not s:
            return None
        
        def decode(substr, times):
            toRet = ''
            nextTimes = i = 0
            while i < len(substr):
                if substr[i] in '123456789':
                    toPass = ''
                    nextTimes = int(substr[i])
                    i+=2
                    while substr[i] != ']':
                        toPass += substr[i]
                        i+=1
                    toRet += decode(toPass, nextTimes)
                else:
                    toRet += substr[i]
                
                i+=1 
            return toRet * times
        # "3[a2[c]]"
        i = 0
        toRet = ''
        while i < len(s):
            if s[i] in '123456789':
                toPass = ''
                nextTimes = int(s[i])
                i+=2
                while s[i] != ']':
                    toPass += s[i]
                    i+=1
                toRet += decode(toPass, nextTimes)
            else:
                toRet += s[i]
            i+=1
        return toRet







                    

        
        