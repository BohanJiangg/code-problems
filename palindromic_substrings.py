# -*- coding: utf-8 -*-
"""
Created on August 14 2019
Leetcode: Palindromic Substrings

Given a string, your task is to count how many palindromic substrings in this string.

The substrings with different start indexes or end indexes are counted as different substrings even they consist of same characters.

Example 1:

Input: "abc"
Output: 3
Explanation: Three palindromic strings: "a", "b", "c".

Example 2:

Input: "baaaa"
dp = [1,1,2,4,6,11]
Output: 6
Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".


Time Complexity O(n^2), worse case where the entire string is a palindrome 
Space Complexity: O(1), keep track of number of palindromes
@author: bohan
"""

class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        if len(s) == 1:
            return 1
        
        cnt = 0
        # find palindromes centered at every character
        for i in range(len(s)):
            # the character itself is a palindrome
            temp = 1
            j = k = i
            while j-1 >= 0 and k+1 < len(s) and s[j-1] == s[k+1]:
                temp+=1
                j-=1
                k+=1

            cnt += temp

        # find even palindromes
        for i in range(1, len(s)):
            temp = 0
            j = k = i
            # only a palindrome if the curr character and preceding characters are equal
            while j-1 >= 0 and k < len(s) and s[j-1] == s[k]:
                temp+=1
                j-=1
                k+=1
            cnt += temp
        
        return cnt
            
    
                

        