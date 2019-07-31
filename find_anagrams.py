# -*- coding: utf-8 -*-
"""
Created on July 29 2019
Leetcode: Merge Intervals

Given a string s and a non-empty string p, find all the start indices of p's anagrams in s.

Strings consists of lowercase English letters only and the length of both strings s and p will not be larger than 20,100.

The order of output does not matter.

Example 1:

Input:
s: "cbaebabacd" p: "abc"

Output:
[0, 6]

Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".

Time Complexity O(n), iterate through s once 
Space Complexity: O(k), where k is the length of p since we maintain 2 dictionaries of length p for the sliding window
@author: bohan
"""
class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        if not s:
            return []
    
        if p == s:
            return [0]

        res = []
        pCounter = Counter(p)
        sCounter = Counter(s[:len(p)-1])
        for i in range(len(p)-1,len(s)):
            sCounter[s[i]] += 1  
            if sCounter == pCounter:   
                res.append(i-len(p)+1)   
            sCounter[s[i-len(p)+1]] -= 1  
            if sCounter[s[i-len(p)+1]] == 0:
                del sCounter[s[i-len(p)+1]]  
        return res





